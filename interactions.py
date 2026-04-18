from sims4.tuning.instances import household
from sims4.tuning.interaction_priority import InteractionPriority
from objects.components.interaction_component import InteractionComponent
from sims4.tuning.interactions import TunableInstantiable
from services import household_manager
from trading_core import get_account, DEFAULT_CRYPTOS
from trading_ui import generate_chart, generate_portfolio_chart

# Interaktions-IDs für die Trading-App
TRADING_INTERACTION_PHONE = "trading_app_phone"
TRADING_INTERACTION_PC = "trading_app_pc"

def on_load():
    """Wird beim Laden des Mods aufgerufen"""
    # Initialisiere das Trading-System
    from trading_core import init
    init()
    
    # Registriere Interaktionen für Handy und PC
    _register_interactions()

def _register_interactions():
    """Registriere die Trading-Interaktionen für Handy und PC"""
    # Diese Funktion würde im echten Mod die TS4-Interaktions-Registry nutzen
    # Beispiel: registry.add_interaction(Phone, TradingAppInteraction)
    pass

def open_trading_app(sim, device_type="phone"):
    """
    Öffne die Trading-App für einen Sim
    
    Args:
        sim: Der Sim der die App öffnet
        device_type: "phone" oder "pc" - bestimmt welches UI gezeigt wird
    """
    household_id = sim.household.id
    account = get_account(household_id)
    
    # Generiere Charts für alle Kryptowährungen
    for crypto_name in DEFAULT_CRYPTOS.keys():
        history = account.price_history.get(crypto_name, [account.prices[crypto_name]])
        generate_chart(crypto_name, history)
    
    # Generiere Portfolio-Übersicht wenn vorhanden
    portfolio_summary = account.get_portfolio_summary()
    if portfolio_summary:
        generate_portfolio_chart(portfolio_summary, account.prices)
    
    # UI öffnen (im echten Mod würde hier das TS4-UI System genutzt)
    # show_ui_screen("ui_trading_screen.xml", data=account_data)
    
    return {
        "household_id": household_id,
        "balance": account.balance,
        "portfolio": portfolio_summary,
        "prices": account.prices,
        "total_value": account.get_total_value(),
        "log": account.log[-10:],  # Letzte 10 Log-Einträge
        "device_type": device_type
    }

def buy_crypto_action(sim, crypto_name, quantity):
    """
    Kaufe Kryptowährung über die App
    
    Args:
        sim: Der Sim der kauft
        crypto_name: Name der Kryptowährung (z.B. "SimCoin")
        quantity: Anzahl die gekauft werden soll
    """
    household_id = sim.household.id
    account = get_account(household_id)
    
    success = account.buy_crypto(crypto_name, quantity)
    
    if success:
        # Aktualisiere Charts nach dem Kauf
        history = account.price_history.get(crypto_name, [])
        generate_chart(crypto_name, history)
        
        return {
            "success": True,
            "message": f"{quantity}x {crypto_name} erfolgreich gekauft!",
            "new_balance": account.balance,
            "new_quantity": account.portfolio.get(crypto_name, 0)
        }
    else:
        return {
            "success": False,
            "message": "Nicht genügend Guthaben oder ungültige Menge!"
        }

def sell_crypto_action(sim, crypto_name, quantity):
    """
    Verkaufe Kryptowährung über die App
    
    Args:
        sim: Der Sim der verkauft
        crypto_name: Name der Kryptowährung
        quantity: Anzahl die verkauft werden soll
    """
    household_id = sim.household.id
    account = get_account(household_id)
    
    success = account.sell_crypto(crypto_name, quantity)
    
    if success:
        return {
            "success": True,
            "message": f"{quantity}x {crypto_name} erfolgreich verkauft!",
            "new_balance": account.balance,
            "remaining_quantity": account.portfolio.get(crypto_name, 0)
        }
    else:
        return {
            "success": False,
            "message": "Nicht genügend Bestand oder ungültige Menge!"
        }

def deposit_funds_action(sim, amount):
    """
    Zahle Simoleons auf das Trading-Konto ein
    
    Args:
        sim: Der Sim der einzahlt
        amount: Betrag der eingezahlt werden soll
    """
    household_id = sim.household.id
    account = get_account(household_id)
    
    success = account.deposit(amount)
    
    if success:
        return {
            "success": True,
            "message": f"{amount}§ erfolgreich eingezahlt!",
            "new_balance": account.balance
        }
    else:
        return {
            "success": False,
            "message": "Nicht genügend Simoleons auf dem Haushaltskonto!"
        }

def withdraw_funds_action(sim, amount):
    """
    Hebe Simoleons vom Trading-Konto ab
    
    Args:
        sim: Der Sim der abhebt
        amount: Betrag der abgehoben werden soll
    """
    household_id = sim.household.id
    account = get_account(household_id)
    
    success = account.withdraw(amount)
    
    if success:
        return {
            "success": True,
            "message": f"{amount}§ erfolgreich abgehoben!",
            "new_balance": account.balance
        }
    else:
        return {
            "success": False,
            "message": "Nicht genügend Guthaben auf dem Trading-Konto!"
        }

def refresh_prices():
    """
    Aktualisiere alle Kurse (wird täglich automatisch aufgerufen)
    """
    from trading_core import update_prices
    update_prices()
    
    # Generiere neue Charts für alle Kryptos
    for crypto_name in DEFAULT_CRYPTOS.keys():
        # Hole Account eines beliebigen Haushalts für die History
        # Im echten Mod müsste man alle Accounts iterieren
        pass

def add_trading_interaction_to_phone(sim):
    """Füge 'Trading-App öffnen' zum Handy-Menü hinzu"""
    # Im echten Mod: Füge Interaktion zur Phone-Registry hinzu
    # phone_interactions.append(TRADING_INTERACTION_PHONE)
    pass

def add_trading_interaction_to_pc(sim):
    """Füge 'Trading-Website öffnen' zum PC-Menü hinzu"""
    # Im echten Mod: Füge Interaktion zur Computer-Registry hinzu
    # computer_interactions.append(TRADING_INTERACTION_PC)
    pass
