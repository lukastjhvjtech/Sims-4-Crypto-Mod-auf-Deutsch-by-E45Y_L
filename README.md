# 📈 Crypto Trading App für Sims 4

Eine Mod die es ermöglicht in Sims 4 in Kryptowährungen zu investieren - über das Handy oder den Computer!

## ✨ Features

### Kryptowährungen
- **5 verschiedene Kryptos** mit realistischen Namen:
  - SimCoin (SIM) - Die Hauptwährung
  - LandgChain (LGC) - Landgraab Crypto
  - PlopsyToken (PLOP) - Plopsy Coin
  - SulaniDoge (SDOGE) - Memecoin
  - GlimmerX (GLX) - Premium Coin

### Tägliches System
- **Automatische Kursaktualisierung** jeden Sim-Tag
- Realistische Preisschwankungen (-10% bis +12% täglich)
- Gelegentliche große Kurssprünge (5% Chance auf +/- 15%)
- 30-Tage Preisverlauf für jede Kryptowährung

### Grafische Darstellung
- **Live-Charts** für jede Kryptowährung
- Farbliche Kennzeichnung (grün = steigend, rot = fallend)
- Prozentuale Veränderungsanzeige
- Portfolio-Übersicht mit Balkendiagramm

### Bedienung
- **Über das Handy**: "Crypto Trader App" öffnen
- **Über den PC**: "Crypto-Trading Website" besuchen
- Einfaches Kaufen und Verkaufen
- Einzahlen und Abheben von Simoleons
- Transaktionsverlauf einsehbar

## 📱 Benutzung

### Erste Schritte
1. Öffne das Handy deines Sims oder einen Computer
2. Wähle "Crypto Trader" aus dem Menü
3. Zahle Startkapital ein (Standard: 1000§ Trading-Guthaben)
4. Kaufe deine ersten Kryptowährungen!

### Trading-Tipps
- Beobachte die Charts bevor du kaufst
- Diversifiziere dein Portfolio
- Verkaufe bei hohen Kursen, kaufe bei tiefen
- Behalte den Überblick über deinen Gesamtgewinn

## 🛠️ Installation

1. Kopiere den gesamten Mod-Ordner nach:
   `Documents/Electronic Arts/The Sims 4/Mods/`
   
2. Aktiviere Mods in den Sims 4 Einstellungen
   
3. Starte das Spiel neu

## 📁 Dateistruktur

```
CryptoTradingMod/
├── __init__.py           # Hauptmodul, lädt die Mod
├── trading_core.py       # Kernlogik (Konten, Preise, Käufe)
├── trading_ui.py         # Chart-Generierung
├── interactions.py       # Handy/PC Interaktionen
├── ui_trading_screen.xml # UI-Layout der App
└── README.md             # Diese Datei
```

## 🔧 Für Modder

Die Mod bietet folgende öffentliche Funktionen:

```python
from CryptoTradingMod.interactions import (
    open_trading_app,
    buy_crypto_action,
    sell_crypto_action,
    deposit_funds_action,
    withdraw_funds_action
)

from CryptoTradingMod.trading_core import get_account

# Account eines Haushalts abrufen
account = get_account(household_id)
print(f"Guthaben: {account.balance}§")
print(f"Portfolio: {account.portfolio}")
```

## ⚠️ Wichtig

- Dies ist eine **Simulations-Mod** - echtes Geld ist nicht involviert
- Alle Kryptowährungen sind fiktiv
- Die Kurse werden zufällig generiert
- Kompatibel mit Sims 4 Version 1.x+

## 🎮 Gameplay

Die Mod fügt ein komplettes Trading-System hinzu:
- Startkapital von 1000§ auf einem separaten Trading-Konto
- Unabhängig vom normalen Haushaltsgeld
- Sicher gespeichert pro Haushalt
- Überlebt Spielstände und Neustarts

Viel Erfolg beim Traden! 🚀📊
