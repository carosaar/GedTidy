# Changelog

## [Unreleased]

## [1.0.1] – 2026‑04‑08
### Geändert
- Statusmeldungen im gesamten Programm vereinheitlicht  
  - `update_status()` zeigt Meldungen nun mit Timeout (10 s) an  
  - Statusmeldungen aus Schritt 1 und beim Import verschwinden automatisch  
- Normwert‑Filterverhalten verbessert  
  - aktuell ausgewählter Normwert bleibt sichtbar, auch wenn er nicht zum Filter passt  
  - neu angelegte Normwerte werden ebenfalls angezeigt, unabhängig vom Filter  
- UI‑Rückmeldungen erweitert  
  - akustisches Signal beim Ein‑ und Ausblenden nicht passender Normwerte  
  - Statusmeldungen informieren über temporär sichtbare bzw. ausgeblendete Normwerte (15s)

### Behoben
- unvollständige Methode `on_details_doubleclick()` korrigiert  
  
---

## [1.0.0] – 2026‑04‑07
### Hinzugefügt
- Erste vollständige README.md mit Installationshinweisen, Systemvoraussetzungen und Projektstruktur
- rootlauncher.py als Startskript für den Entwicklungsmodus
- Grundlegende GUI-Struktur mit PySide6
- Öffnen und Anzeigen von GEDCOM-Dateien
- Normalisierung bestimmter Werte (z. B. Ortsangaben)
- PyInstaller-Konfiguration (GedTidy.spec)
- Template für Installer (template.iss), jedoch nicht Bestandteil des Repositories
- Windows‑Sicherheits-Hinweise (SmartScreen, Ransomware-Schutz, Ordnerschutz)
- Abschnitt „Mögliche Weiterentwicklungen“

### Geändert
- README.md überarbeitet und erweitert
- Projektstruktur bereinigt und dokumentiert

### Entfernt
- Build‑Artefakte (dist/, installer/) aus dem Repository ausgeschlossen

---

## [0.1.0] – Initialer Entwicklungsstand
### Hinzugefügt
- Grundgerüst des Projekts
- Basis-UI
- Versionierungssystem
- Prototyping