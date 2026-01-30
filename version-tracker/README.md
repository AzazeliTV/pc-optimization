# Version Tracker

Desktop-App zum Verwalten und Prüfen von Software/Treiber-Versionen.

## Features

- Liste aller Software mit Versionen
- Direkt-Links zu Download-Seiten
- "Zuletzt geprüft" Datum
- Warnung wenn >30 Tage nicht geprüft
- Daten werden lokal gespeichert (versions.json)

## Installation

### Option 1: Python direkt ausführen

```bash
pip install PyQt6
python version_tracker.py
```

### Option 2: Als .exe bauen (Windows)

1. Python 3.10+ installieren
2. `build.bat` doppelklicken
3. `.exe` liegt dann im `dist` Ordner

## Benutzung

1. **Version eintragen**: Klicke in die "Meine Version" Spalte
2. **Update prüfen**: Klicke auf 🔗 um die Download-Seite zu öffnen
3. **Alle prüfen**: Öffnet alle Download-Seiten auf einmal
4. **Software hinzufügen**: ➕ Button für eigene Software

## Screenshot

```
┌─────────────────────────────────────────────────────────────┐
│  🖥️ Version Tracker                                         │
├─────────────────────────────────────────────────────────────┤
│  📊 15 Software | ✅ 10 OK | ⚠️ 3 nie geprüft | 🔴 2 überfällig │
├─────────────────────────────────────────────────────────────┤
│  Software          │ Version │ Geprüft    │ Status  │ 🔗 🗑️ │
│  ─────────────────────────────────────────────────────────  │
│  NVIDIA Treiber    │ 572.16  │ 29.01.2026 │ 🟢 1 Tag │      │
│  AMD Chipset       │ 6.05.28 │ 15.01.2026 │ 🟡 14 T  │      │
│  BIOS X870E        │ 2503    │ 01.12.2025 │ 🔴 60 T  │      │
│  ...               │         │            │         │      │
└─────────────────────────────────────────────────────────────┘
```

## Daten

Alle Daten werden in `versions.json` gespeichert (gleicher Ordner wie die App).
