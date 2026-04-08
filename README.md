# GedTidy – Genealogical Data Cleaner

**GedTidy**[^1] ist ein Werkzeug zur Analyse und Normalisierung genealogischer **GEDCOM‑Dateien**.  
Es richtet sich an Anwenderinnen und Anwender, die bereits **ausreichende Kenntnisse des GEDCOM‑Standards** besitzen.  
Ohne ein grundlegendes Verständnis der GEDCOM‑Struktur können Analyseergebnisse falsch interpretiert werden.

> **Wichtiger Hinweis:**  
> Die Nutzung erfolgt auf eigene Verantwortung.  
> Es wird **keinerlei Haftung für Schäden** an Daten oder Systemen übernommen.  
> Details siehe **MIT‑Lizenz**.

---

## 🚀 Funktionen

- Öffnen und Analysieren von GEDCOM‑Dateien  
- Normalisierung bestimmter Werte (z.B. Ortsangaben)  
- Moderne, klare graphische Benutzeroberfläche  
- Vollständig lokale Verarbeitung – **keine Datenübertragung**  
- Windows‑Installer/Deinstaller inklusive Desktop‑Verknüpfung

## 📖 Benutzerhandbuch und Testumgebung
Das vollständige Benutzerhandbuch befindet sich im Ordner [`doc/`](doc/).  
Es enthält eine ausführliche Beschreibung der Funktionen, Beispiele und Hinweise zur Nutzung von GedTidy.
Eine Testdatei ist unter [`testdata/`](testdata/).
-> [Handbuch](doc/HANDBUCH.md) 

---

## 🖥️ Systemvoraussetzungen

- **Windows 10 oder Windows 11**
- Keine zusätzliche Software erforderlich  
  (Python ist nicht notwendig – GedTidy wird als Windows EXE ausgeliefert)
- Eine Kompilierung unter Linux oder anderen Plattformen ist möglich, wird hier jedoch nicht beschrieben.

---

### ⚠️ Windows blockiert Installation oder Ausführung?

Windows kann die Installation oder Ausführung blockieren, weil:

- die Anwendung nicht signiert ist  
- der SmartScreen‑Filter unbekannte Programme standardmäßig blockiert  
- der Download aus dem Internet stammt  
- der **Ransomware‑Schutz (Controlled Folder Access)** den Zugriff verhindert  
- der **Ordnerschutz** bestimmte Verzeichnisse sperrt

Typische Meldungen:

- „Windows hat Ihren PC geschützt“  
- „Die Ausführung wurde aus Sicherheitsgründen blockiert“  
- „Unbekannter Herausgeber“  
- „Diese App wurde durch den Ransomware‑Schutz blockiert“  
- „Der Zugriff auf den geschützten Ordner wurde blockiert“

---

### ✔ Mögliche Lösungen

1. **SmartScreen‑Dialog erweitern**  
   - Auf „Weitere Informationen“ klicken  
   - Dann „Trotzdem ausführen“

2. **Datei‑Eigenschaften prüfen**  
   - Rechtsklick → Eigenschaften  
   - Haken setzen bei „Zulassen“ (falls vorhanden)

3. **Download‑Ordner vermeiden**  
   - Datei in einen anderen Ordner verschieben  
   - Dann erneut starten

4. **Antivirus‑Software prüfen**  
   - Manche Scanner blockieren unbekannte EXE‑Dateien  
   - GedTidy enthält keine Netzwerk‑ oder Update‑Funktionen

5. **Ransomware‑Schutz (Controlled Folder Access) erlaubt die App nicht**  
   - Windows‑Sicherheit öffnen  
   - „Viren‑ & Bedrohungsschutz“ → „Ransomware‑Schutz verwalten“  
   - „Zugriff durch kontrollierten Ordner“ → „Zulässige Apps“  
   - `GedTidy.exe` als zulässige App hinzufügen

6. **Ordnerschutz blockiert Datei‑Zugriffe**  
   - GedTidy als zulässige App im Ordnerschutz eintragen  
   - oder Dateien in einen nicht geschützten Ordner verschieben

7. **Letzte Möglichkeit: Anwendung selbst kompilieren**  
   - Wenn Windows die Ausführung dauerhaft verhindert, kann GedTidy jederzeit **aus dem Quellcode selbst kompiliert** werden  
   - Hinweise dazu finden sich im Abschnitt **„Entwicklung“**

---

## 📁 Projektstruktur

```
GedTidy/
├── assets/               # Icons und statische Ressourcen
├── doc/                  # Dokumentationen und Handbuch
├── src/
│   └── gedtidy/
│       ├── ui/           # Qt UI-Module
│       ├── models/       # Datenmodelle
│       ├── main.py       # Einstiegspunkt der Anwendung
│       └── version.py    # Versionsverwaltung
├── testdata/             # Beispiel-ged
├── tools/                # Versionsverwaltung
├── GedTidy.spec          # PyInstaller-Konfiguration
├── requirements.txt
├── rootlauncher.py       # Startscript für den Entwicklungsmodus
├── LICENSE
├── pyproject.toml
└── README.md
```

*Anmerkung:*
`rootlauncher.py` dient als Startskript (Wrapper) für den Entwicklungsmodus und ermöglicht den direkten Aufruf der Anwendung über `python rootlauncher.py`. 

---

## 🔧 Entwicklung

### Voraussetzungen

- Python 3.11+
- Abhängigkeiten installieren (aktuell nur PySide6):

```bash
pip install -r requirements.txt
```

---

### Start im Entwicklungsmodus

```bash
python src/gedtidy/main.py
```

oder

```bash
python rootlauncher.py
```

---

## 🛠️ Build-Prozess

### EXE erzeugen

```bash
pyinstaller GedTidy.spec
```

### Installierbare Version erzeugen

Die Erstellung eines Installers ist optional und nicht Bestandteil dieses Repositories.
Entwickler können GedTidy direkt aus dem Quellcode kompilieren oder bei Bedarf einen eigenen Installer verwenden.

---

## 📝 Lizenz

Dieses Projekt steht unter der [**MIT License**](LICENSE).
Die Lizenz erlaubt freie Nutzung, Modifikation und Weitergabe,  
**schließt jedoch jede Haftung aus**.

---

## 👤 Autor

**Dieter Eckstein**  
GitHub: [https://github.com/carosaar](https://github.com/carosaar)

---

## 💬 Feedback & Beiträge

Fehler, Wünsche oder Ideen?  
Einfach ein Issue im Repository eröffnen oder einen Pull Request stellen.

---

## 🌱 Mögliche Weiterentwicklungen

GedTidy befindet sich in aktiver Entwicklung. Die folgenden Ideen skizzieren mögliche zukünftige Erweiterungen:

- **- Intelligente Normalisierung**  
  Erkennung potenzieller Inkonsistenzen, z. B. unterschiedliche Schreibweisen, Schreibfehler.

- **Mehrsprachige Benutzeroberfläche**  
  Unterstützung weiterer Sprachen neben Deutsch.

- **Automatische Backups**  
  automatische Sicherung des Arbeitsstandes beim Export der normierten ged-Datei.



[^1]: **GedTidy** setzt sich aus zwei Teilen zusammen:
**GED** – die übliche Abkürzung für **GEDCOM**, das genealogische Datenaustauschformat  
**Tidy** – englisch für **aufräumen**, **bereinigen**, **ordnen**
Der Name bedeutet also sinngemäß: 👉 **„GEDCOM‑Dateien aufräumen und sauber machen“**
