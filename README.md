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

### 🆕 Trading-Fähigkeit (Skill-System)
- **10 Skill-Level** von "Anfänger" bis "Legendär"
- **XP sammeln** durch:
  - Erste Einzahlung (+5 XP)
  - Krypto-Käufe (+10 XP)
  - Krypto-Verkäufe (+15 XP)
  - Profitable Trades (+25 XP)
  - Portfolio-Meilensteine (bis zu +500 XP)
- **Level-Boni**:
  - Level 1: Keine Gebühren
  - Level 2: +2% bessere Kaufpreise
  - Level 3: +5% bessere Kaufpreise
  - Level 5: +12% bessere Kaufpreise
  - Level 10: +35% bessere Kaufpreise!
- **Freischaltbare Features**:
  - Preis-Charts (Level 2)
  - Portfolio-Analyse (Level 3)
  - Tägliche Prognosen (Level 4)
  - Erweiterte Charts (Level 5)
  - Risiko-Analyse (Level 6)
  - Automatische Alerts (Level 7)
  - Premium-Analysen (Level 8)
  - Exklusive Coins (Level 9)
  - Alle Features (Level 10)

### 🏦 Zwischenkonto-System
- **Separates Trading-Konto** - unabhängig vom Haushaltsgeld
- **Startguthaben: 0§** - du musst erst Geld einzahlen!
- Einzahlen vom Haushaltskonto jederzeit möglich
- Gewinne zurück aufs Haushaltskonto übertragbar
- Alle Transaktionen werden protokolliert

### 📌 Pinnwand-Protokoll
- **Alle Transaktionen** erscheinen auf der Pinnwand:
  - Einzahlungen/Abhebungen
  - Käufe/Verkäufe mit Details
  - Tägliche Kursaktualisierungen
  - Skill Level-Ups mit Boni-Anzeige
  - Portfolio-Meilensteine
- Zeitstempel für jede Aktion
- Übersichtlicher Verlauf aller Aktivitäten

## 📱 Benutzung

### Erste Schritte
1. Öffne das Handy deines Sims oder einen Computer
2. Wähle "Crypto Trader" aus dem Menü
3. **Zahle Startkapital ein** (du beginnst mit 0§!)
4. Kaufe deine ersten Kryptowährungen!
5. Sammle XP und steige im Level auf!

### Trading-Tipps
- Beobachte die Charts bevor du kaufst
- Diversifiziere dein Portfolio
- Verkaufe bei hohen Kursen, kaufe bei tiefen
- Behalte den Überblick über deinen Gesamtgewinn
- Steige im Level auf für bessere Preise!

## 🛠️ Installation

1. Kopiere den gesamten Mod-Ordner nach:
   `Documents/Electronic Arts/The Sims 4/Mods/`
   
2. Aktiviere Mods in den Sims 4 Einstellungen
   
3. Starte das Spiel neu

## 📁 Dateistruktur

```
CryptoTradingMod/
├── __init__.py           # Hauptmodul, lädt die Mod
├── trading_core.py       # Kernlogik (Konten, Preise, Käufe, Skills)
├── trading_skill.py      # Skill-Definitionen (Level, XP, Boni)
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
from CryptoTradingMod.trading_skill import get_skill_level, SKILL_LEVELS

# Account eines Haushalts abrufen
account = get_account(household_id)
print(f"Guthaben: {account.balance}§")
print(f"Portfolio: {account.portfolio}")
print(f"Trading XP: {account.trading_xp}")

# Skill-Info
skill_info = account.get_skill_info()
print(f"Level: {skill_info['level']} - {skill_info['name']}")
print(f"Bonus: {skill_info['bonus']}")
```

## ⚠️ Wichtig

- Dies ist eine **Simulations-Mod** - echtes Geld ist nicht involviert
- Alle Kryptowährungen sind fiktiv
- Die Kurse werden zufällig generiert
- Kompatibel mit Sims 4 Version 1.x+

## 🎮 Gameplay

Die Mod fügt ein komplettes Trading-System hinzu:
- **Start bei 0§** auf einem separaten Trading-Konto
- Unabhängig vom normalen Haushaltsgeld
- Sicher gespeichert pro Haushalt
- Überlebt Spielstände und Neustarts
- Skill-System mit 10 Leveln und progressiven Boni
- Automatische Protokollierung aller Aktionen auf der Pinnwand

Viel Erfolg beim Traden! 🚀📊

