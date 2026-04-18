import sims4
import services
from . import trading_core
from .interactions import on_load as interactions_on_load

MOD_ID = "Lukas_CryptoTradingMod"
MOD_NAME = "Crypto Trading App"
MOD_VERSION = "1.0"

def on_load():
    """Wird beim Laden des Mods aufgerufen"""
    if not trading_core.is_initialized():
        trading_core.init()
        sims4.log.info(MOD_ID, f"{MOD_NAME} v{MOD_VERSION} geladen!")
        sims4.log.info(MOD_ID, "Krypto-Trading jetzt verfügbar über Handy und PC!")
    
    # Rufe Interaktionen-Initialisierung auf
    interactions_on_load()

def on_unload():
    """Wird beim Entladen des Mods aufgerufen"""
    sims4.log.info(MOD_ID, f"{MOD_NAME} entladen.")

# Täglicher Update-Hook für Kursaktualisierungen
_last_check_date = None

def _check_daily_update():
    """Überprüfe ob ein neuer Sim-Tag begonnen hat und aktualisiere Kurse"""
    global _last_check_date
    
    zone = services.current_zone()
    if not zone:
        return
    
    current_date = zone.sim_date
    
    # Nur einmal pro Sim-Tag aktualisieren
    if _last_check_date != current_date:
        sims4.log.info(MOD_ID, f"Tagesupdate für Krypto-Kurse ({current_date})")
        trading_core.update_prices()
        _last_check_date = current_date

# Hook in den Game-Tick einhängen (alle 60 Sekunden prüfen)
sims4.utils.run_at_interval(_check_daily_update, seconds=60)

# Helper-Funktion für andere Mods/Scripts
def get_trading_account(household_id):
    """Gib das Trading-Konto für einen Haushalt zurück"""
    return trading_core.get_account(household_id)
