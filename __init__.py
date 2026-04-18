import sims4
import services
from . import trading_core

MOD_ID = "Lukas_TradingMod"

def on_load():
    if not trading_core.is_initialized():
        trading_core.init()
        sims4.log.info(MOD_ID, "TradingMod loaded successfully.")

def on_unload():
    sims4.log.info(MOD_ID, "TradingMod unloaded.")

# Täglicher Update-Hook (sauber an TS4 gekoppelt)
def _check_daily_update():
    zone = services.current_zone()
    if not zone:
        return
    current_date = zone.sim_date
    if trading_core.last_update_date != current_date:
        trading_core.update_prices()
        trading_core.last_update_date = current_date

# Hook in den Game-Tick einhängen
sims4.utils.run_at_interval(_check_daily_update, seconds=30)
