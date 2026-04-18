# Crypto Trading App für Sims 4

Eine vollständige Mod für Die Sims 4, die ein realistisches Kryptowährungs-Trading-System hinzufügt.

## 🚀 Features

### 💰 Trading-System
- **5 Kryptowährungen**: SimCoin, LandgChain, PlopsyToken, SulaniDoge, GlimmerX
- **Tägliche Kursaktualisierungen**: Realistische Schwankungen (-10% bis +12%)
- **Zwischenkonto-System**: Du musst erst Geld auf dein Trading-Konto einzahlen
- **Startguthaben**: 0§ - aktives Einzahlen erforderlich!

### ⭐ Trading-Fähigkeit (Skill)
- **10 Level**: Anfänger → Lernender → Einsteiger → Handelnder → Fortgeschrittener → Experte → Profi → Veteran → Master → Legendär
- **XP-System**:
  - Erste Einzahlung: +5 XP
  - Krypto kaufen: +10 XP
  - Krypto verkaufen: +15 XP
  - Profitable Trades: +25 XP
  - Portfolio-Meilensteine: +100 bis +500 XP

- **Level-Boni** (bessere Kaufpreise):
  - Level 1: 0% Rabatt
  - Level 2: 2% Rabatt
  - Level 3: 5% Rabatt
  - Level 5: 12% Rabatt
  - Level 10: 35% Rabatt!

### 📊 Grafische Darstellung
- **Kurs-Charts**: Zeigt die Preisentwicklung jeder Kryptowährung
- **Portfolio-Übersicht**: Visuelle Darstellung deiner Assets
- **Farbcodierung**: Grün bei steigenden, rot bei fallenden Kursen

### 📱 Plattformen
- **Handy-App**: Trading über das Smartphone-Menü
- **Computer**: Trading über den Browser am PC

### 📌 Pinnwand-Protokoll
Alle Aktivitäten werden automatisch protokolliert:
- ✅ Einzahlungen/Abhebungen mit Betrag
- ✅ Käufe/Verkäufe mit Details und Skill-Bonus-Anzeige
- ✅ Tägliche Kursaktualisierungen
- ✅ LEVEL-UP Benachrichtigungen mit neuem Bonus
- ✅ Portfolio-Meilensteine (1.000§, 10.000§, 100.000§)

## 📁 Installation

### WICHTIG: Ordnerstruktur!
Sims 4 kann Skript-Mods nur laden, wenn sie sich **maximal einen Ordner tief** im Mods-Verzeichnis befinden.

#### Korrekte Installation:
```
Dokumente/Electronic Arts/Die Sims 4/Mods/
├── __init__.py          ← HIER (oder in einem Unterordner)
├── trading_core.py      ← HIER
├── trading_skill.py     ← HIER
├── interactions.py      ← HIER
├── trading_ui.py        ← HIER
└── TradingData/         ← Dieser Ordner wird automatisch erstellt
```

#### FALSCH (zu tief verschachtelt):
```
Dokumente/Electronic Arts/Die Sims 4/Mods/
└── Crypto-Trading-App-f-r-Sims-4-main/  ← ZU TIEF!
    └── Crypto-Trading-App-f-r-Sims-4-main/
        └── __init__.py
```

### Schritte:
1. Alle `.py`-Dateien direkt in den `Mods`-Ordner kopieren (oder in EINEN Unterordner)
2. Sicherstellen, dass keine Sonderzeichen im Ordnernamen sind
3. Im Spiel unter "Optionen" → "Sonstiges":
   - ✅ "Benutzerdefinierte Inhalte und Mods zulassen" aktivieren
   - ✅ "Skript-Mods zulassen" aktivieren
4. "Änderungen anwenden" klicken und Spiel neu starten
5. Cache löschen (optional aber empfohlen):
   - `localthumbcache.package` im Sims 4 Hauptordner löschen
   - `cache`-Ordner im Sims 4 Hauptordner leeren

## 🎮 gameplay

### Erster Start:
1. Öffne die Trading-App auf deinem Handy oder Computer
2. Zahle Geld vom Haushaltskonto auf dein Trading-Konto ein (mindestens 100§ empfohlen)
3. Kaufe deine erste Kryptowährung (SimCoin ist gut für Anfänger)
4. Beobachte die Kursentwicklung täglich

### Tipps:
- **Diversifiziere**: Kaufe verschiedene Kryptos statt alles in eine zu investieren
- **Geduld**: Kurse schwanken täglich - verkaufe nicht bei jedem Dip
- **Skill-Level**: Je höher dein Level, desto besser deine Kaufpreise
- **Meilensteine**: Erreiche Portfolio-Ziele für Bonus-XP

## 🔧 Technische Details

### Dateien:
- `__init__.py`: Hauptmodul mit Lade-/Entladefunktionen
- `trading_core.py`: Kernlogik (Accounts, Transaktionen, Preisupdates)
- `trading_skill.py`: Skill-System mit 10 Leveln und XP-Berechnung
- `interactions.py`: Interaktionen für Handy und PC
- `trading_ui.py`: Chart-Generierung (PNG-Bilder)
- `TradingData/`: Automatisch erstellter Speicherordner für Savegames

### Kompatibilität:
- ✅ MC Command Center
- ✅ XML Injector
- ✅ SAC Zombie Apocalypse
- ✅ Extreme Violence
- ✅ Die meisten anderen Mods (keine XML-Overrides)

## 🐛 Fehlerbehebung

### Mod wird nicht geladen:
1. Überprüfe die Ordnerstruktur (siehe Installation)
2. Lösche `localthumbcache.package`
3. Stelle sicher, dass Skript-Mods aktiviert sind
4. Prüfe die Spielversion (Mod benötigt neuestes Update)

### Keine Benachrichtigungen:
- Das ist normal, wenn die Pinnwand-Funktion nicht verfügbar ist
- Alle Aktionen werden trotzdem im internen Log gespeichert

### Charts werden nicht angezeigt:
- Stelle sicher, dass PIL/Pillow installiert ist (im echten Mod enthalten)
- Überprüfe Schreibrechte im Mods-Ordner

## 📝 Changelog

### Version 1.0
- ✅ Vollständiges Trading-System mit 5 Kryptowährungen
- ✅ Zwischenkonto-System (0§ Startguthaben)
- ✅ 10-Level Skill-System mit XP und Boni
- ✅ Tägliche Kursaktualisierungen
- ✅ Grafische Charts für Kurse und Portfolio
- ✅ Pinnwand-Protokoll für alle Aktionen
- ✅ Handy- und PC-Unterstützung
- ✅ Portfolio-Meilensteine
- ✅ Level-Up Benachrichtigungen

## 📄 Lizenz

Diese Mod ist kostenlos für den persönlichen Gebrauch.  
Weiterverbreitung nur mit Quellenangabe erlaubt.

## 👨‍💻 Support

Bei Fragen oder Problemen:
1. Überprüfe zuerst diese README
2. Lösche Cache und starte neu
3. Überprüfe die Ordnerstruktur
4. Aktiviere Skript-Mods in den Einstellungen

---

**Viel Erfolg beim Traden! 🚀📈**
