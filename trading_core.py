import json
import os
import random
import services
from sims4.common import SimSpentCurrency

MOD_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TradingData")
os.makedirs(MOD_DATA_DIR, exist_ok=True)

# Standard-Kryptowährungen mit realistischen Namen und Startpreisen
DEFAULT_CRYPTOS = {
    "SimCoin": 25.00,      # Hauptwährung
    "LandgChain": 45.50,   # Landgraab Crypto
    "PlopsyToken": 8.75,   # Plopsy Coin
    "SulaniDoge": 0.50,    # Memecoin
    "GlimmerX": 120.00,    # Premium Coin
}

class TradingAccount:
    def __init__(self, household_id):
        self.household_id = household_id
        self.balance = 1000  # Startkapital im Zwischenkonto (Simoleons)
        self.portfolio = {}  # {"SimCoin": 10, "LandgChain": 0}
        self.prices = DEFAULT_CRYPTOS.copy()
        self.log = []        # ["[08:00] 500§ eingezahlt", ...]
        self.price_history = {} # {"SimCoin": [12.1, 12.5, 11.8, ...]}
        self._load()

    def deposit(self, amount):
        """Zahle Simoleons vom Haushalt auf das Trading-Konto ein"""
        hh = services.household_manager().get(self.household_id)
        if hh and hh.money >= amount:
            hh.money -= amount
            self.balance += amount
            self.log.append(f"[{self._timestamp()}] {amount}§ auf Trading-Konto eingezahlt")
            self._save()
            return True
        return False

    def withdraw(self, amount):
        """Hebe Simoleons vom Trading-Konto ab"""
        if self.balance >= amount:
            hh = services.household_manager().get(self.household_id)
            if hh:
                self.balance -= amount
                hh.money += amount
                self.log.append(f"[{self._timestamp()}] {amount}§ vom Trading-Konto abgehoben")
                self._save()
                return True
        return False

    def buy_crypto(self, crypto_name, qty):
        """Kaufe Kryptowährung"""
        if qty <= 0:
            return False
        cost = self.prices.get(crypto_name, 0) * qty
        if self.balance >= cost:
            self.balance -= cost
            self.portfolio[crypto_name] = self.portfolio.get(crypto_name, 0) + qty
            self.log.append(f"[{self._timestamp()}] {qty}x {crypto_name} für {cost:.2f}§ gekauft @ {self.prices[crypto_name]:.2f}§/Stk")
            self._save()
            return True
        return False

    def sell_crypto(self, crypto_name, qty):
        """Verkaufe Kryptowährung"""
        if qty <= 0 or self.portfolio.get(crypto_name, 0) < qty:
            return False
        revenue = self.prices.get(crypto_name, 0) * qty
        self.balance += revenue
        self.portfolio[crypto_name] -= qty
        if self.portfolio[crypto_name] <= 0:
            del self.portfolio[crypto_name]
        self.log.append(f"[{self._timestamp()}] {qty}x {crypto_name} für {revenue:.2f}§ verkauft @ {self.prices[crypto_name]:.2f}§/Stk")
        self._save()
        return True

    def update_daily(self):
        """Aktualisiere alle Kurse täglich mit realistischer Volatilität"""
        for crypto in self.prices:
            # Realistischere Preisänderungen: -10% bis +12%
            change = random.uniform(-0.10, 0.12)
            
            # Gelegentliche größere Sprünge (5% Chance für +/- 15%)
            if random.random() < 0.05:
                change = random.uniform(-0.15, 0.15)
            
            new_price = max(0.01, self.prices[crypto] * (1 + change))
            self.prices[crypto] = round(new_price, 2)
            
            # Verlauf speichern (letzte 30 Tage)
            if crypto not in self.price_history:
                self.price_history[crypto] = []
            self.price_history[crypto].append(new_price)
            if len(self.price_history[crypto]) > 30:
                self.price_history[crypto].pop(0)
        
        self.log.append(f"[{self._timestamp()}] Tageskurse aktualisiert")
        self._save()

    def get_total_value(self):
        """Berechne Gesamtwert (Kontostand + Portfolio-Wert)"""
        portfolio_value = sum(
            self.portfolio.get(crypto, 0) * self.prices.get(crypto, 0)
            for crypto in self.portfolio
        )
        return self.balance + portfolio_value

    def get_portfolio_summary(self):
        """Gib Übersicht des Portfolios zurück"""
        summary = []
        for crypto, qty in self.portfolio.items():
            current_price = self.prices.get(crypto, 0)
            value = qty * current_price
            summary.append({
                "name": crypto,
                "quantity": qty,
                "price": current_price,
                "value": value
            })
        return summary

    def _save(self):
        path = os.path.join(MOD_DATA_DIR, f"household_{self.household_id}.json")
        with open(path, "w") as f:
            json.dump({
                "balance": self.balance,
                "portfolio": self.portfolio,
                "prices": self.prices,
                "log": self.log,
                "history": self.price_history
            }, f, indent=2)

    def _load(self):
        path = os.path.join(MOD_DATA_DIR, f"household_{self.household_id}.json")
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
            self.balance = data.get("balance", 1000)
            self.portfolio = data.get("portfolio", {})
            self.prices = data.get("prices", DEFAULT_CRYPTOS.copy())
            self.log = data.get("log", [])
            self.price_history = data.get("history", {})
        else:
            # Initialisiere Preisverlauf für neue Accounts
            for crypto in self.prices:
                self.price_history[crypto] = [self.prices[crypto]]

    def _timestamp(self):
        zone = services.current_zone()
        if zone:
            return str(zone.sim_date).replace(" ", "-")
        return "??"


# Globale Variablen für daily tracking
last_update_date = None
_accounts = {}  # Cache für Accounts

def get_account(household_id):
    """Hole oder erstelle Trading-Account für Haushalt"""
    if household_id not in _accounts:
        _accounts[household_id] = TradingAccount(household_id)
    return _accounts[household_id]

def init():
    """Initialisiere das Trading-System"""
    global last_update_date
    zone = services.current_zone()
    if zone:
        last_update_date = zone.sim_date

def update_prices():
    """Update alle Accounts täglich"""
    for account in _accounts.values():
        account.update_daily()
