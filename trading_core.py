import json
import os
import random
import services

MOD_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TradingData")
os.makedirs(MOD_DATA_DIR, exist_ok=True)

class TradingAccount:
    def __init__(self, household_id):
        self.household_id = household_id
        self.balance = 1000  # Startkapital im Zwischenkonto
        self.portfolio = {}  # {"SimTech": 10, "Landgraab": 0}
        self.prices = {}     # {"SimTech": 15.50, ...}
        self.log = []        # ["[08:00] 500§ eingezahlt", ...]
        self.price_history = {} # {"SimTech": [12.1, 12.5, 11.8, ...]}
        self._load()

    def deposit(self, amount):
        hh = services.household_manager().get(self.household_id)
        if hh.money >= amount:
            hh.money -= amount
            self.balance += amount
            self.log.append(f"[{self._timestamp()}] {amount}§ auf Trading-Konto eingezahlt")
            self._save()
            return True
        return False

    def buy(self, stock, qty):
        cost = self.prices.get(stock, 0) * qty
        if self.balance >= cost:
            self.balance -= cost
            self.portfolio[stock] = self.portfolio.get(stock, 0) + qty
            self.log.append(f"[{self._timestamp()}] {qty}x {stock} für {cost:.2f}§ gekauft")
            self._save()
            return True
        return False

    def update_daily(self):
        for stock in self.prices:
            change = random.uniform(-0.08, 0.10)
            new_price = max(1.0, self.prices[stock] * (1 + change))
            self.prices[stock] = round(new_price, 2)
            if stock not in self.price_history:
                self.price_history[stock] = []
            self.price_history[stock].append(new_price)
            if len(self.price_history[stock]) > 30:
                self.price_history[stock].pop(0)
        self.log.append(f"[{self._timestamp()}] Kurse aktualisiert")
        self._save()

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
            self.prices = data.get("prices", {"SimTech": 15.50, "Landgraab": 42.10, "Plopsy": 8.30})
            self.log = data.get("log", [])
            self.price_history = data.get("history", {})

    def _timestamp(self):
        zone = services.current_zone()
        if zone:
            return str(zone.sim_date).replace(" ", "-")
        return "??"
