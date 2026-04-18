import json
import os
import random
import services
from sims4.common import SimSpentCurrency
from trading_skill import get_skill_level, get_price_bonus, XP_REWARDS

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
        self.balance = 0  # Startkapital im Zwischenkonto (Simoleons) - jetzt 0 statt 1000
        self.portfolio = {}  # {"SimCoin": 10, "LandgChain": 0}
        self.prices = DEFAULT_CRYPTOS.copy()
        self.log = []        # ["[08:00] 500§ eingezahlt", ...]
        self.price_history = {} # {"SimCoin": [12.1, 12.5, 11.8, ...]}
        self.trading_xp = 0  # XP für die Trading-Fähigkeit
        self.total_invested = 0  # Gesamt investiertes Geld (für Milestones)
        self.profitable_trades = 0  # Anzahl profitabler Trades
        self._load()

    def deposit(self, amount):
        """Zahle Simoleons vom Haushalt auf das Trading-Konto ein"""
        hh = services.household_manager().get(self.household_id)
        if hh and hh.money >= amount:
            hh.money -= amount
            self.balance += amount
            log_entry = f"[{self._timestamp()}] {amount}§ auf Trading-Konto eingezahlt"
            self.log.append(log_entry)
            self._post_to_bulletin_board(log_entry)
            
            # XP für Einzahlung (tägliches Login Bonus)
            self.add_xp(XP_REWARDS["daily_login"])
            
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
                log_entry = f"[{self._timestamp()}] {amount}§ vom Trading-Konto abgehoben"
                self.log.append(log_entry)
                self._post_to_bulletin_board(log_entry)
                self._save()
                return True
        return False

    def buy_crypto(self, crypto_name, qty):
        """Kaufe Kryptowährung"""
        if qty <= 0:
            return False
        cost = self.prices.get(crypto_name, 0) * qty
        
        # Skill-Bonus anwenden (besserer Preis bei höherem Level)
        skill_level = get_skill_level(self.trading_xp)
        price_bonus = get_price_bonus(skill_level)
        discounted_cost = cost * (1 - price_bonus)
        
        if self.balance >= discounted_cost:
            self.balance -= discounted_cost
            self.portfolio[crypto_name] = self.portfolio.get(crypto_name, 0) + qty
            self.total_invested += discounted_cost
            
            savings = cost - discounted_cost
            log_entry = f"[{self._timestamp()}] {qty}x {crypto_name} für {discounted_cost:.2f}§ gekauft @ {self.prices[crypto_name]:.2f}§/Stk"
            if savings > 0:
                log_entry += f" (Skill-Bonus: {savings:.2f}§ gespart!)"
            
            self.log.append(log_entry)
            self._post_to_bulletin_board(log_entry)
            
            # XP für Kauf
            self.add_xp(XP_REWARDS["buy_crypto"])
            
            # Check for first trade milestone
            if self.total_invested <= discounted_cost:  # Erster Trade
                self.add_xp(XP_REWARDS["first_trade"])
            
            # Check portfolio milestones
            self._check_portfolio_milestones()
            
            self._save()
            return True
        return False

    def sell_crypto(self, crypto_name, qty):
        """Verkaufe Kryptowährung"""
        if qty <= 0 or self.portfolio.get(crypto_name, 0) < qty:
            return False
        
        # Ursprünglichen Kaufpreis für Profit-Berechnung speichern
        original_price = self.prices.get(crypto_name, 0)
        revenue = original_price * qty
        
        self.balance += revenue
        self.portfolio[crypto_name] -= qty
        if self.portfolio[crypto_name] <= 0:
            del self.portfolio[crypto_name]
        
        log_entry = f"[{self._timestamp()}] {qty}x {crypto_name} für {revenue:.2f}§ verkauft @ {self.prices[crypto_name]:.2f}§/Stk"
        self.log.append(log_entry)
        self._post_to_bulletin_board(log_entry)
        
        # XP für Verkauf
        self.add_xp(XP_REWARDS["sell_crypto"])
        
        # Check for profitable trade (einfache Logik: wenn mehr als Kaufpreis)
        # In einer komplexeren Version würde man den durchschnittlichen Kaufpreis tracken
        self.profitable_trades += 1
        if self.profitable_trades % 5 == 0:  # Jeder 5. Trade als "profitabel" markiert
            self.add_xp(XP_REWARDS["profitable_trade"])
            milestone_log = f"[{self._timestamp()}] Profitabler Trade Bonus!"
            self.log.append(milestone_log)
            self._post_to_bulletin_board(milestone_log)
        
        # Check portfolio milestones
        self._check_portfolio_milestones()
        
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
        
        log_entry = f"[{self._timestamp()}] Tageskurse aktualisiert"
        self.log.append(log_entry)
        self._post_to_bulletin_board(log_entry)
        self._save()

    def _check_portfolio_milestones(self):
        """Überprüfe Portfolio-Meilensteine und vergebe XP"""
        total_value = self.get_total_value()
        
        if total_value >= 100000 and not hasattr(self, '_milestone_100k'):
            self.add_xp(XP_REWARDS["portfolio_milestone_100k"])
            self._milestone_100k = True
            log_entry = f"[{self._timestamp()}] Meilenstein erreicht: Portfolio über 100.000§!"
            self.log.append(log_entry)
            self._post_to_bulletin_board(log_entry)
        
        if total_value >= 10000 and not hasattr(self, '_milestone_10k'):
            self.add_xp(XP_REWARDS["portfolio_milestone_10k"])
            self._milestone_10k = True
            log_entry = f"[{self._timestamp()}] Meilenstein erreicht: Portfolio über 10.000§!"
            self.log.append(log_entry)
            self._post_to_bulletin_board(log_entry)
        
        if total_value >= 1000 and not hasattr(self, '_milestone_1k'):
            self.add_xp(XP_REWARDS["portfolio_milestone_1k"])
            self._milestone_1k = True
            log_entry = f"[{self._timestamp()}] Meilenstein erreicht: Portfolio über 1.000§!"
            self.log.append(log_entry)
            self._post_to_bulletin_board(log_entry)

    def add_xp(self, amount):
        """Füge XP zur Trading-Fähigkeit hinzu"""
        old_level = get_skill_level(self.trading_xp)
        self.trading_xp += amount
        new_level = get_skill_level(self.trading_xp)
        
        # Level-Up Benachrichtigung
        if new_level > old_level:
            from trading_skill import get_level_info
            level_info = get_level_info(new_level)
            
            log_entry = f"[{self._timestamp()}] LEVEL-UP! Trading-Fähigkeit: {level_info['name']} (Level {new_level})"
            self.log.append(log_entry)
            self._post_to_bulletin_board(log_entry)
            
            bonus_log = f"Neuer Bonus: {level_info['bonus']} - Freigeschaltet: {level_info['unlock']}"
            self.log.append(bonus_log)
            self._post_to_bulletin_board(bonus_log)
            
            # Maximallevel erreicht?
            if new_level == 10:
                self.add_xp(XP_REWARDS["max_level_reached"])
                max_log = f"[{self._timestamp()}] LEGENDÄRER TRADER erreicht! Du beherrschst die Märkte!"
                self.log.append(max_log)
                self._post_to_bulletin_board(max_log)
        
        self._save()

    def get_skill_info(self):
        """Gib Informationen zur Trading-Fähigkeit zurück"""
        level = get_skill_level(self.trading_xp)
        from trading_skill import get_level_info, get_xp_for_next_level
        
        level_info = get_level_info(level)
        next_level_xp = get_xp_for_next_level(level)
        
        return {
            "level": level,
            "xp": self.trading_xp,
            "name": level_info["name"],
            "description": level_info["description"],
            "bonus": level_info["bonus"],
            "unlock": level_info["unlock"],
            "next_level_xp": next_level_xp,
            "xp_to_next": next_level_xp - self.trading_xp if next_level_xp else 0
        }

    def _post_to_bulletin_board(self, message):
        """Poste eine Nachricht an die Pinnwand (Bulletin Board)"""
        try:
            from ui.ui_dialog_notification import UiDialogNotification
            from event_testing.resolver import SingleSimResolver
            
            # Hole den ersten Sim im Haushalt für die Benachrichtigung
            hh = services.household_manager().get(self.household_id)
            if hh and len(hh.sim_info_list) > 0:
                sim_info = hh.sim_info_list[0]
                resolver = SingleSimResolver(sim_info)
                
                # Erstelle eine Benachrichtigung für die Pinnwand
                notification = UiDialogNotification(
                    sim_info,
                    resolver,
                    title="Crypto Trading Update",
                    text=message,
                    icon=None
                )
                notification.show_dialog()
        except Exception as e:
            # Falls Pinnwand nicht verfügbar, einfach im Log belassen
            pass

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
                "history": self.price_history,
                "trading_xp": self.trading_xp,
                "total_invested": self.total_invested,
                "profitable_trades": self.profitable_trades,
                "milestones": {
                    "milestone_1k": hasattr(self, '_milestone_1k'),
                    "milestone_10k": hasattr(self, '_milestone_10k'),
                    "milestone_100k": hasattr(self, '_milestone_100k')
                }
            }, f, indent=2)

    def _load(self):
        path = os.path.join(MOD_DATA_DIR, f"household_{self.household_id}.json")
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
            self.balance = data.get("balance", 0)
            self.portfolio = data.get("portfolio", {})
            self.prices = data.get("prices", DEFAULT_CRYPTOS.copy())
            self.log = data.get("log", [])
            self.price_history = data.get("history", {})
            self.trading_xp = data.get("trading_xp", 0)
            self.total_invested = data.get("total_invested", 0)
            self.profitable_trades = data.get("profitable_trades", 0)
            
            # Meilensteine wiederherstellen
            milestones = data.get("milestones", {})
            if milestones.get("milestone_1k"):
                self._milestone_1k = True
            if milestones.get("milestone_10k"):
                self._milestone_10k = True
            if milestones.get("milestone_100k"):
                self._milestone_100k = True
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
