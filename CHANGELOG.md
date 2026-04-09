# Changelog

## [Unreleased]

## [1.0.2] – 2026‑04‑09

### Geändert
- Menüstruktur überarbeitet:
  - Menü „Datei“ in „Arbeitsstand“ umbenannt.
  - „Info“ und „Beenden“ als eigene Menüs auf oberster Ebene.
  - Filterfelder für alle drei Tabellen mit Clear-Buttons.
  - Default-Name beim Export des Arbeitsstandes: <myged>_<TAG>.tidy
- Step 1 (Load & Extract):
  - TAG-Auswahl und aktuelle Einstellungen (TAG, Modus, Separator) mit Standardwerten gefüllt (TAG=`PLAC`, Modus=`Gesamt`).
  Step 2 (Normalize):
  - Drei-Tabellen-Layout mit stabiler Filter- und Sortierlogik.
  - Neue Proxy-Klasse `NormProxy`, die den aktuellen Normwert auch bei aktivem Filter sichtbar hält.
  - Statusmeldungen und optionaler Beep, wenn Normwerte durch Filterlogik ausgeblendet oder temporär angezeigt werden.
- Step 3 (Write Output):
  - Ersetzungstabelle wird beim Öffnen von Step 3 automatisch nach Normwert (Spalte 0) sortiert.

### Behoben
- "Verschwinden" von Normwerten bei Filterung beseitigt.



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