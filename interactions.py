from sims4.tuning.instances import household
from sims4.tuning.interaction_priority import InteractionPriority
from objects.components.interaction_component import InteractionComponent
from sims4.tuning.interactions import TunableInstantiable
from services import household_manager

def on_load():
    # Trigger für tägliches Update
    # (Im echten Mod über ZoneDirector.on_tick oder daily_sim_update registrieren)
    pass

def add_trading_interaction(target_sim):
    # Hier würdest du die offizielle TS4-Interaktions-Registry nutzen
    # Beispiel-Stub: Fügt "Trading-App öffnen" zum Handy/PC hinzu
    pass
