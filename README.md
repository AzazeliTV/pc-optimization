# Ultimate Gaming PC Optimization Guide

Dein persönlicher Guide für die optimale Einrichtung deines Gaming-PCs.

**Live:** https://azazelitv.github.io/pc-optimization/

---

## Schnell-Bearbeitung

### Hardware ändern (z.B. neue GPU)

1. Öffne `index.html`
2. Suche nach `<!-- Section: Hardware -->`
3. Finde die entsprechende Karte und ändere den Text:

```html
<!-- GPU Beispiel -->
<p class="font-semibold text-white">MSI RTX 4080 Super Gaming X Trio</p>
<!-- Ändern zu: -->
<p class="font-semibold text-white">NVIDIA RTX 5090 Founders Edition</p>
```

### Neue Sektion hinzufügen

Kopiere dieses Template und füge es vor `<!-- Footer -->` ein:

```html
<!-- Section: DEINE SEKTION -->
<section id="deine-id" class="py-12 scroll-mt-8">
  <div class="section-header">
    <div class="section-icon">
      <i data-lucide="ICON-NAME" class="w-6 h-6 text-accent-primary"></i>
    </div>
    <div>
      <h2 class="text-3xl font-bold text-white">Titel</h2>
      <p class="text-gray-500 text-sm mt-1">Untertitel</p>
    </div>
  </div>

  <!-- Dein Inhalt hier -->
</section>
```

Vergiss nicht, auch einen Link in der Sidebar hinzuzufügen:
```html
<a href="#deine-id" class="nav-link flex items-center gap-3 text-sm font-medium">
  <i data-lucide="ICON-NAME" class="w-4 h-4"></i>
  <span>Dein Link</span>
</a>
```

### Icons finden

Alle verfügbaren Icons: https://lucide.dev/icons/

Häufig verwendete:
- `cpu` - Prozessor
- `monitor` - Bildschirm
- `hard-drive` - Speicher
- `settings` - Einstellungen
- `keyboard` - Tastatur
- `mouse` - Maus
- `headphones` - Headset
- `gamepad-2` - Gaming
- `zap` - Strom/Performance
- `alert-triangle` - Warnung

---

## Komponenten

### Karte (Card)

```html
<div class="card rounded-2xl p-5 flex items-center gap-4">
  <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-accent-primary/20 to-accent-primary/5 flex items-center justify-center">
    <i data-lucide="cpu" class="w-6 h-6 text-accent-primary"></i>
  </div>
  <div class="flex-1">
    <p class="text-xs text-gray-500 mb-1">Label</p>
    <p class="font-semibold text-white">Titel</p>
  </div>
</div>
```

### Tabelle

```html
<div class="table-modern bg-dark-800/50">
  <table class="w-full text-sm">
    <thead>
      <tr>
        <th class="text-left px-5 py-4">Spalte 1</th>
        <th class="text-left px-5 py-4">Spalte 2</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="px-5 py-4 text-white">Wert 1</td>
        <td class="px-5 py-4 text-gray-400">Wert 2</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Warnung (Alert)

```html
<!-- Warnung (gelb) -->
<div class="alert alert-warning">
  <i data-lucide="alert-triangle" class="w-5 h-5 text-accent-warning flex-shrink-0"></i>
  <p class="text-sm">Deine Warnung hier</p>
</div>

<!-- Gefahr (rot) -->
<div class="alert alert-danger">
  <i data-lucide="alert-octagon" class="w-5 h-5 text-accent-danger flex-shrink-0"></i>
  <p class="text-sm">Wichtiger Hinweis</p>
</div>

<!-- Info (grün) -->
<div class="alert alert-info">
  <i data-lucide="lightbulb" class="w-5 h-5 text-accent-primary flex-shrink-0"></i>
  <p class="text-sm">Hilfreicher Tipp</p>
</div>
```

### Code-Block

```html
<div class="bg-dark-900 rounded-lg p-3 font-mono text-xs text-accent-primary overflow-x-auto">
  <code>dein befehl hier</code>
</div>
```

---

## Farben

| Name | Wert | Verwendung |
|------|------|------------|
| `accent-primary` | `#00ff88` | Hauptfarbe (Grün) |
| `accent-secondary` | `#00d4ff` | Zweitfarbe (Cyan) |
| `accent-warning` | `#ffaa00` | Warnungen (Orange) |
| `accent-danger` | `#ff4466` | Fehler (Rot) |
| `accent-purple` | `#aa44ff` | Akzent (Lila) |

---

## Dateistruktur

```
pc-optimization/
├── index.html          # Haupt-Guide (alles in einer Datei)
├── README.md           # Diese Anleitung
├── CHANGELOG.md        # Versionshistorie
└── data/               # JSON-Dateien (Referenz für Updates)
    ├── hardware.json
    ├── software.json
    ├── peripherals.json
    ├── wooting-profiles.json
    └── ...
```

---

## Deployment

Nach Änderungen:

1. Änderungen speichern
2. Git commit: `git add . && git commit -m "Beschreibung"`
3. Git push: `git push origin main`
4. Warten (~1 Min) bis GitHub Pages aktualisiert

---

## Troubleshooting

### Icons werden nicht angezeigt
- Prüfe ob der Icon-Name korrekt ist: https://lucide.dev/icons/
- Icons sind case-sensitive (`Menu` ≠ `menu`)

### Styles funktionieren nicht
- Tailwind-Klassen müssen exakt sein
- Cache leeren: `Strg + Shift + R`

### Seite lädt nicht
- Prüfe die Browser-Konsole (F12) auf Fehler
- JavaScript-Fehler können das Laden blockieren
