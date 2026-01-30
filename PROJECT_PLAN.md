# Ultimate Gaming PC Optimization Guide - Projektplan

## Projektübersicht

Ziel: Komplette Überarbeitung des Gaming PC Optimization Guides mit:
- Professionellem Design (Tailwind CSS + echte Icons)
- Modularer Dateistruktur für einfache Updates
- Changelog-System für Versionierung
- Vollständige, verifizierte Informationen mit offiziellen Links
- Wooting 80HE Import-Codes

---

## Dein System (Hardware-Referenz)

| Komponente | Modell | Status |
|------------|--------|--------|
| CPU | AMD Ryzen 7 9800X3D | Top 1% Gaming CPU |
| GPU | MSI RTX 4080 Super Gaming X Trio | High-End |
| RAM | G.Skill 64GB DDR5-6000 CL30 | Optimal für AM5 |
| Mainboard | Gigabyte X670 Gaming X AX | Stabil |
| SSD | Samsung 990 PRO 2TB | NVMe Gen4 |
| CPU-Kühler | Corsair H150i Elite Capellix XT | 360mm AIO |
| Netzteil | be quiet! 1000W Gold | Ausreichend |
| Keyboard | Wooting 80HE | Beste Gaming-Tastatur |
| Monitor 1 | ASUS ROG SWIFT OLED PG32UCDMR | 4K 240Hz QD-OLED |
| Monitor 2 | Alienware AW2723DF | QHD 280Hz |
| Monitor 3 | Gigabyte M28U | 4K 144Hz |

---

## Neue Website-Architektur

### Dateistruktur
```
pc-optimization/
├── index.html                 # Hauptseite
├── CHANGELOG.md               # Versionshistorie
├── PROJECT_PLAN.md            # Dieser Plan
├── README.md                  # Projektbeschreibung
│
├── css/
│   └── custom.css             # Custom Styles (zusätzlich zu Tailwind)
│
├── js/
│   ├── main.js                # Hauptlogik
│   ├── checklist.js           # Checklisten mit localStorage
│   └── search.js              # Suchfunktion
│
├── data/
│   ├── hardware.json          # Hardware-Konfiguration (leicht editierbar)
│   ├── software.json          # Software-Links
│   ├── bios-settings.json     # BIOS-Einstellungen
│   ├── windows-tweaks.json    # Windows-Optimierungen
│   ├── nvidia-settings.json   # NVIDIA-Einstellungen
│   └── wooting-profiles.json  # Wooting-Profile mit Import-Codes
│
└── assets/
    └── icons/                 # Lokale Icon-Kopien (optional)
```

### Technologie-Stack
- **Tailwind CSS** (via CDN) - Utility-First CSS
- **Lucide Icons** - 1,500+ saubere SVG-Icons
- **Vanilla JavaScript** - Kein Framework nötig
- **JSON-Daten** - Einfach editierbar für Updates

### Design-Konzept
- Dark Gaming Theme (Schwarz/Cyan/Grün)
- Glassmorphism-Effekte
- Smooth Animations
- Mobile-Responsive
- Print-freundlich

---

## Recherche-Ergebnisse

### 1. AMD Ryzen 7 9800X3D - BIOS Optimierung

#### PBO (Precision Boost Overdrive) Settings
| Einstellung | Empfohlener Wert | Erklärung |
|-------------|------------------|-----------|
| PBO | Advanced | Volle Kontrolle |
| PBO Limits | Motherboard | Nutzt Mainboard-Limits |
| Max CPU Boost Clock Override | +200 MHz | Erhöht Boost bis ~5.45 GHz |
| PBO Scalar | 1x - 10x | Start mit 1x, erhöhen wenn stabil |

#### Curve Optimizer Settings
| Einstellung | Startpunkt | Optimiert |
|-------------|------------|-----------|
| Mode | All Cores | Per-Core für Maximum |
| Sign | Negative | Undervolting |
| Magnitude | -15 bis -20 | Konservativ starten! |
| Max stabil (typisch) | -25 bis -30 | Mit guter Kühlung möglich |

**Wichtig:** Jede CPU ist unterschiedlich! -30 bei einem User kann bei dir crashen.

#### Stabilitätstests (in dieser Reihenfolge)
1. Cinebench R23 (Multi-Core, 10 Min)
2. OCCT CPU Test (30 Min)
3. Y-Cruncher (verschiedene Modi)
4. Gaming (mehrere Stunden)
5. Idle + Sleep/Wake Test

#### Global C-State Control (KRITISCH!)
```
Pfad: Settings → AMD CBS → SMU Common Options → CPPC
Einstellung: Global C-State Control
Wert: Enabled (NICHT Auto!)
```
**Eliminiert Micro-Stuttering bei X3D CPUs!**

**Quellen:**
- [Overclock.net - 9800X3D Curve Optimizer Tips](https://www.overclock.net/threads/9800x3d-curve-optimizer-tips.1814218/)
- [SkatterBencher - 9800X3D Overclocked to 5750 MHz](https://skatterbencher.com/2024/11/06/skatterbencher-82-ryzen-7-9800x3d-overclocked-to-5750-mhz/)
- [Tom's Hardware Forum - 9800X3D CO/PBO Tuning](https://forums.tomshardware.com/threads/ryzen-7-9800x3d-co-pbo-tuning-unstable-voltage-spikes-at-lighter-co-settings.3889438/)

---

### 2. Windows 11 24H2 - Gaming Optimierung

#### VBS Komplett Deaktivieren (5-25% mehr FPS!)

**Schritt 1: Memory Integrity deaktivieren**
```
Einstellungen → Datenschutz & Sicherheit → Windows-Sicherheit
→ Gerätesicherheit → Kernisolierung → Details
→ Speicherintegrität → AUS
```

**Schritt 2: Tamper Protection deaktivieren**
```
Windows-Sicherheit → Viren- & Bedrohungsschutz
→ Einstellungen verwalten → Manipulationsschutz → AUS
```

**Schritt 3: VBS via Registry deaktivieren (Admin CMD)**
```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard" /v EnableVirtualizationBasedSecurity /t REG_DWORD /d 0 /f
```

**Schritt 4: Windows Hello VBS-Abhängigkeit deaktivieren (NEU für 24H2!)**
```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\WindowsHello" /v Enabled /t REG_DWORD /d 0 /f
```

**Schritt 5: Hypervisor deaktivieren**
```cmd
bcdedit /set hypervisorlaunchtype off
```

**Prüfen:** `msinfo32` → "Virtualization-based security" = "Not enabled"

#### Warnung: Anti-Cheat Kompatibilität
Einige Spiele mit Anti-Cheat (z.B. Riot Vanguard 2.0) benötigen VBS! Prüfe vor dem Deaktivieren.

#### Weitere Windows-Optimierungen
| Einstellung | Pfad | Wert |
|-------------|------|------|
| Game Mode | Einstellungen → Gaming | EIN |
| HAGS | System → Bildschirm → Grafik | EIN |
| Optimierungen für Fenstermodus | System → Bildschirm → Grafik | **AUS** (Stutter Fix!) |
| Xbox Game Bar | Einstellungen → Gaming | AUS |
| Hintergrundaufnahme | Einstellungen → Gaming → Aufnahmen | AUS |

#### Ultimate Performance Power Plan aktivieren
```cmd
powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
```
Dann in Systemsteuerung → Energieoptionen auswählen.

**Quellen:**
- [Windows Forum - Disabling VBS for Better Gaming Performance](https://windowsforum.com/threads/windows-11-24h2-disabling-vbs-for-better-gaming-performance.343305/)
- [ElevenForum - How to disable VBS on 24H2](https://www.elevenforum.com/t/how-to-disable-virtualization-based-security-vbs-on-24h2.39269/)
- [Tom's Hardware - VBS Performance Impact](https://www.tomshardware.com/news/windows-vbs-harms-performance-rtx-4090)

---

### 3. NVIDIA RTX 4080 Super - Control Panel Settings

#### Globale 3D-Einstellungen
| Einstellung | Wert | Erklärung |
|-------------|------|-----------|
| Energieverwaltungsmodus | Maximale Leistung bevorzugen | Verhindert GPU Downclocking |
| Modus für geringe Latenz | Ein (nicht Ultra) | Ultra kann Probleme verursachen |
| Vertikale Synchronisierung | Ein | Mit G-Sync + Frame Cap |
| Max. Bildfrequenz | 237 FPS | 240Hz - 3 für G-Sync Headroom |
| Shader-Cache-Größe | 100 GB / Unbegrenzt | Verhindert Shader-Stutter |
| Texturfilterung - Qualität | Hohe Leistung | Minimal sichtbarer Unterschied |
| Anisotrope Filterung | 16x | Kein Performance-Impact |
| Bildscharfzeichnung | Ein (0.50) | Optional |
| Max. Bildfrequenz Hintergrund | 30 FPS | Spart Strom bei Alt-Tab |
| Virtual Reality Pre-Rendered Frames | 1 | Reduziert Latenz |

#### G-Sync Konfiguration (für 240Hz OLED)
1. Anzeige → G-SYNC einrichten
2. "G-SYNC, G-SYNC-kompatibel aktivieren" → Häkchen
3. "Für Fenstermodus und Vollbild aktivieren"
4. ASUS OLED als primären G-Sync Monitor wählen

#### Optimale Kombination für niedrigste Latenz
```
G-Sync: EIN
V-Sync (NVCP): EIN
Max Frame Rate: 237 (3 unter Refresh Rate)
Low Latency Mode: EIN
In-Game V-Sync: AUS
```

**Quellen:**
- [Games Req - Best NVIDIA Control Panel Settings](https://gamesreq.com/best-nvidia-control-panel-settings-for-gaming-updated-yearly/)
- [Modern Gamer - Best NVIDIA 4000 Series Settings](https://moderngamer.com/best-nvidia-4000-series-gpu-settings-for-gaming-performance/)
- [Overclock.net - NVIDIA Control Panel Best Settings](https://www.overclock.net/threads/best-nvidia-control-panel-settings.1814470/)

---

### 4. Wooting 80HE - Optimierte Profile

#### Basis-Einstellungen (Global)
| Einstellung | Wert |
|-------------|------|
| Polling Rate | 8000 Hz (8kHz) |
| Tachyon Mode | EIN (reduziert Latenz) |
| Rapid Trigger | Aktiviert |
| Firmware | Aktuellste Version |

#### FPS Competitive (CS2, Valorant)
| Einstellung | Wert | Hinweis |
|-------------|------|---------|
| Actuation Point (WASD) | 0.1mm | Schnellste Reaktion |
| Rapid Trigger Sensitivity | 0.2 - 0.4mm | Für Counter-Strafing |
| Continuous RT | AN (WASD) | Wichtig! |
| Rappy Snappy | AN | Counter-Strafe Boost |
| Spacebar | 2.0mm | Verhindert versehentliche Sprünge |

#### Wootabase Import-Codes
- **CS2:** [BEST CS2 SETTINGS BY WOOTING](https://wootabase.com/profile/5de7a9b20bbef678f8aadc77e982386cc3f4)
- **Valorant:** [FPS Rapid Trigger Profile](https://wootabase.com/profile/f8e85ca041a8787333aa8502da524aa4bb50)
- **Valorant Radiant:** [Radiant Valorant Profile](https://wootabase.com/profile/502a0236cc59e21126ba066c0576375ef4e8)
- **CS2 Design:** [80HE CS2 Design](https://wootabase.com/profile/67f593b260b63980da1eb825f5c9cd6e3a7b)

#### TenZ Settings
[Offizielle TenZ x Wooting Settings](https://wooting.io/ambassadors/tenz)

**Hinweis:** Einige Features wie Rappy Snappy sind in CS2 verboten! Prüfe die Regeln.

**Quellen:**
- [Wooting - Rapid Trigger Guide](https://wooting.io/rapid-trigger)
- [Wootabase - Community Profiles](https://wootabase.com)
- [ProSettings - Wooting 80HE Review](https://prosettings.net/reviews/wooting-80he/)

---

### 5. Software & Download-Links

#### System-Treiber
| Software | Zweck | Offizieller Download |
|----------|-------|---------------------|
| AMD Chipset Driver | CPU-Treiber + 3D V-Cache Optimizer | [amd.com/support](https://www.amd.com/en/support) |
| NVIDIA App | GPU-Treiber | [nvidia.com/download](https://www.nvidia.com/download/index.aspx) |

#### Monitoring & Tools
| Software | Zweck | Offizieller Download |
|----------|-------|---------------------|
| HWiNFO64 | System Monitoring | [hwinfo.com](https://www.hwinfo.com/download/) |
| GPU-Z | GPU Info | [techpowerup.com](https://www.techpowerup.com/gpuz/) |
| CPU-Z | CPU Info | [cpuid.com](https://www.cpuid.com/softwares/cpu-z.html) |

#### Treiber-Management
| Software | Zweck | Offizieller Download |
|----------|-------|---------------------|
| DDU | Display Driver Uninstaller | [guru3d.com](https://www.guru3d.com/files-details/display-driver-uninstaller-download.html) |
| NVCleanstall | NVIDIA Driver Customizer | [techpowerup.com](https://www.techpowerup.com/nvcleanstall/) |

#### Hardware-Software
| Software | Zweck | Offizieller Download |
|----------|-------|---------------------|
| Samsung Magician | SSD Management | [samsung.com](https://semiconductor.samsung.com/consumer-storage/support/tools/) |
| Corsair iCUE | AIO-Steuerung | [corsair.com/icue](https://www.corsair.com/icue) |
| DisplayWidget Center | OLED Monitor | [asus.com/support](https://www.asus.com/support/) |
| Wootility | Wooting Config | [wootility.io](https://wootility.io) |

#### Benchmarking
| Software | Zweck | Download |
|----------|-------|----------|
| Cinebench R23/2024 | CPU Benchmark | [maxon.net](https://www.maxon.net/cinebench) |
| 3DMark | GPU Benchmark | [Steam](https://store.steampowered.com/app/223850/3DMark/) |
| OCCT | Stabilitätstest | [ocbase.com](https://www.ocbase.com/) |
| AIDA64 | Memory Benchmark | [aida64.com](https://www.aida64.com/downloads) |
| TestMem5 | RAM Stabilitätstest | [github.com](https://github.com/integralfx/MemTestHelper) |

#### Streaming
| Software | Zweck | Offizieller Download |
|----------|-------|---------------------|
| OBS Studio | Streaming/Recording | [obsproject.com](https://obsproject.com/) |
| StreamElements | OBS Plugin | [streamelements.com](https://streamelements.com/obslive) |

---

### 6. Icon-Library Entscheidung

#### Empfehlung: Lucide Icons
- **1,500+ Icons** - Ausreichend für alle Kategorien
- **Konsistentes Design** - Sauber und modern
- **MIT Lizenz** - Frei nutzbar
- **Leichtgewichtig** - Tree-shaking Support
- **CDN verfügbar** - Einfache Einbindung

#### Alternative: Tabler Icons
- **5,600+ Icons** - Mehr Auswahl
- **24x24 Grid** - Pixel-perfekt
- **Gut für Dashboards**

#### Einbindung (CDN)
```html
<!-- Lucide Icons -->
<script src="https://unpkg.com/lucide@latest"></script>
<script>lucide.createIcons();</script>

<!-- Usage -->
<i data-lucide="cpu"></i>
<i data-lucide="monitor"></i>
<i data-lucide="keyboard"></i>
```

---

## Changelog-System

### Format (CHANGELOG.md)
```markdown
# Changelog

## [2.1.0] - 2026-02-XX
### Added
- Neue Wooting Profile Import-Codes
- RTX 5000 Serie Support vorbereitet

### Changed
- NVIDIA Settings für Treiber 5XX.XX aktualisiert
- Windows 11 24H2 Tweaks erweitert

### Fixed
- VBS Deaktivierung für neueste Windows-Version

## [2.0.0] - 2026-01-30
### Added
- Komplettes Redesign mit Tailwind CSS
- Modulare JSON-Datenstruktur
- Suchfunktion
- Echte SVG-Icons (Lucide)
```

---

## Nächste Schritte

### Phase 1: Grundstruktur (Heute)
- [x] Projektplan erstellen
- [ ] Dateistruktur anlegen
- [ ] Tailwind + Lucide Setup
- [ ] Basis-HTML-Template

### Phase 2: Content Migration
- [ ] Alle Sektionen übertragen
- [ ] JSON-Dateien erstellen
- [ ] Links verifizieren
- [ ] Neue Recherche-Infos einarbeiten

### Phase 3: Features
- [ ] Interaktive Checklisten
- [ ] Suchfunktion
- [ ] Print-Styles
- [ ] Dark/Light Toggle (optional)

### Phase 4: Polish
- [ ] Mobile-Optimierung
- [ ] Performance-Test
- [ ] Cross-Browser-Test
- [ ] Finale Review

---

## Wartungsplan

### Bei Windows-Updates
1. VBS-Methode prüfen
2. Neue Tweaks recherchieren
3. Changelog aktualisieren

### Bei Treiber-Updates
1. NVIDIA Settings prüfen
2. AMD Chipset testen
3. Download-Links verifizieren

### Bei Hardware-Tausch
1. hardware.json aktualisieren
2. Neue Komponenten-Sektion hinzufügen
3. Alte Settings als "Legacy" markieren

### Monatlich
1. Wooting Firmware-Check
2. SSD Health prüfen
3. Temperatur-Logs reviewen

---

*Erstellt: 2026-01-30*
*Guide Version: 2.0 (in Entwicklung)*
