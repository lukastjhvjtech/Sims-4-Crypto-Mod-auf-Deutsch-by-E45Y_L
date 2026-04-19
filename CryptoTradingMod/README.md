# Crypto Trading App für Sims 4 - Vollständige Mod

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
- **Kurs-Charts**: Zeigt die Preisentwicklung jeder Kryptowährung (wenn PIL installiert ist)
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
└── sims4crypto/                    ← EIN Ordner tief!
    ├── __init__.ts4script
    ├── trading_core.ts4script
    ├── trading_skill.ts4script
    ├── interactions.ts4script
    └── trading_ui.ts4script
```

#### FALSCH (zu tief verschachtelt):
```
Dokumente/Electronic Arts/Die Sims 4/Mods/
└── Crypto-Trading-App/             ← ZU TIEF!
    └── Crypto-Trading-App/
        └── __init__.ts4script
```

### Schritte:

1. **Alle `.ts4script`-Dateien in EINEN Unterordner kopieren** (`sims4crypto`)
2. **Sicherstellen, dass keine Sonderzeichen im Ordnernamen sind**
3. **Im Spiel unter "Optionen" → "Sonstiges":**
   - ✅ "Benutzerdefinierte Inhalte und Mods zulassen" aktivieren
   - ✅ "Skript-Mods zulassen" aktivieren
4. **"Änderungen anwenden" klicken und Spiel neu starten**
5. **Cache löschen (optional aber empfohlen):**
   - `localthumbcache.package` im Sims 4 Hauptordner löschen
   - `cache`-Ordner im Sims 4 Hauptordner leeren

## 🎮 Gameplay

### Erster Start:

1. **Öffne die Trading-App** auf deinem Handy oder Computer
   - Handy: Telefon-Menü → "Crypto Trading"
   - Computer: Webbrowser → "Crypto Trading Platform"

2. **Zahle Geld** vom Haushaltskonto auf dein Trading-Konto ein (mindestens 100§ empfohlen)

3. **Kaufe deine erste Kryptowährung** (SimCoin ist gut für Anfänger)

4. **Beobachte die Kursentwicklung** täglich

### Tipps:

- **Diversifiziere**: Kaufe verschiedene Kryptos statt alles in eine zu investieren
- **Geduld**: Kurse schwanken täglich - verkaufe nicht bei jedem Dip
- **Skill-Level**: Je höher dein Level, desto besser deine Kaufpreise
- **Meilensteine**: Erreiche Portfolio-Ziele für Bonus-XP

## 🔧 Technische Details

### Dateien:

| Datei | Beschreibung |
|-------|-------------|
| `__init__.ts4script` | Hauptmodul mit Lade-/Entladefunktionen und Hooks |
| `trading_core.ts4script` | Kernlogik (Accounts, Transaktionen, Preisupdates) |
| `trading_skill.ts4script` | Skill-System mit 10 Leveln und XP-Berechnung |
| `interactions.ts4script` | Interaktionen für Handy und PC |
| `trading_ui.ts4script` | Chart-Generierung (PNG-Bilder, optional mit PIL) |

### Kompatibilität:

- ✅ MC Command Center
- ✅ XML Injector
- ✅ SAC Zombie Apocalypse
- ✅ Extreme Violence
- ✅ Die meisten anderen Mods (keine XML-Overrides)

## 🐛 Fehlerbehebung

### Mod wird nicht geladen:

1. Überprüfe die Ordnerstruktur (maximal 1 Ordner tief!)
2. Lösche `localthumbcache.package`
3. Stelle sicher, dass Skript-Mods aktiviert sind
4. Prüfe die Spielversion (Mod benötigt neuestes Update)
5. Überprüfe `LastException.txt` auf Fehler

### Keine Interaktionen im Handy/PC sichtbar:

1. **Warte 1-2 Minuten** nach dem Laden des Spiels
2. **Klicke auf das Objekt** (Handy/PC) und warte auf das Menü
3. **Scrolle im Menü** - die Option könnte weiter unten sein
4. **Teste ohne andere Mods** um Konflikte auszuschließen

### Charts werden nicht angezeigt:

- Das ist normal wenn PIL/Pillow nicht verfügbar ist
- Alle Funktionen bleiben nutzbar, nur die grafischen Charts fehlen
- Die Text-basierte Anzeige funktioniert immer

### Keine Benachrichtigungen:

- Das kann vorkommen wenn die UI-Dialoge blockiert werden
- Alle Aktionen werden trotzdem im internen Log gespeichert
- Über das Menü "Verlauf" kannst du alle Transaktionen sehen

## 📝 Changelog

### Version 1.0
- ✅ Vollständiges Trading-System mit 5 Kryptowährungen
- ✅ Zwischenkonto-System (0§ Startguthaben)
- ✅ 10-Level Skill-System mit XP und Boni
- ✅ Tägliche Kursaktualisierungen
- ✅ Text-basierte Charts (PIL optional)
- ✅ Pinnwand-Protokoll für alle Aktionen
- ✅ Handy- und PC-Unterstützung
- ✅ Portfolio-Meilensteine
- ✅ Level-Up Benachrichtigungen

## 📄 Lizenz

Diese Mod ist kostenlos für den persönlichen Gebrauch.  
Weiterverbreitung nur mit Quellenangabe erlaubt.

## 👨‍💻 Support

Bei Fragen oder Problemen:

1. Überprüfe zuerst die INSTALLATION.txt
2. Lösche Cache und starte neu
3. Überprüfe die Ordnerstruktur
4. Aktiviere Skript-Mods in den Einstellungen
5. Prüfe LastException.txt auf Fehlermeldungen

---

**Viel Erfolg beim Traden! 🚀📈**
