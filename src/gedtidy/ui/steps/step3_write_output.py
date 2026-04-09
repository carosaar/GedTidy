import os
import re
from datetime import datetime

from PySide6.QtWidgets import (
    QWidget, QHeaderView,
    QFileDialog, QMessageBox, QAbstractItemView
)
from PySide6.QtCore import Qt

from gedtidy.ui.steps.step3_write_output_ui import Ui_Step3_WriteOutput
from gedtidy.ui.widgets.text_item import TextItem
from gedtidy.ui.widgets.numeric_item import NumericItem
from gedtidy.version import APP_VERSION


class Step3_WriteOutput(QWidget):
    """
    Step 3 – Zusammenfassung + Ersetzungstabelle + Export
    Nicht editierbare Tabellen, aber vollständig markierbar.
    """

    def __init__(self, model, rohdaten, tag, original_path,
                 separator, single_value_mode, parent=None):
        super().__init__(parent)

               
        self.ui = Ui_Step3_WriteOutput()
        self.ui.setupUi(self)
        self.ui.edit_filter_replacements.setClearButtonEnabled(True)


        # Daten aus Step 1 + Step 2
        self.model = model
        self.rohdaten = rohdaten
        self.tag = tag
        self.original_path = original_path
        self.separator = separator
        self.single_value_mode = single_value_mode

        self.output_path = None

        # UI initialisieren
        self.init_ui()
        self.connect_signals()

        # Filter
        self.ui.edit_filter_replacements.textChanged.connect(self.apply_filter)

    # ------------------------------------------------------------
    # UI INITIALISIERUNG
    # ------------------------------------------------------------
    def init_ui(self):
        if hasattr(self.ui, "tabWidget"):
            self.ui.tabWidget.setCurrentIndex(0)

        self.update_summary()
        self.configure_table()
        self.fill_replacements_table()
        self._update_filtered_sum_label()

    # ------------------------------------------------------------
    # TABELLENKONFIGURATION
    # ------------------------------------------------------------

    def configure_table(self):
        table = self.ui.table_replacements

        # Keine blaue Markierung
        table.setStyleSheet("""
            QTableWidget::item:selected {
                background: transparent;
                color: black;
            }
            QTableWidget::item {
                selection-background-color: transparent;
                selection-color: black;
            }
        """)

        # Kein Fokus-Rahmen
        # table.setFocusPolicy(Qt.NoFocus)

        # Auswahlverhalten
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)


        table.verticalHeader().setVisible(False)

        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)

        table.setSortingEnabled(True)
        table.sortByColumn(0, Qt.AscendingOrder)


    # ------------------------------------------------------------
    # SIGNALVERBINDUNGEN
    # ------------------------------------------------------------
    def connect_signals(self):
        self.ui.btn_write.clicked.connect(self.on_write_clicked)

    # ------------------------------------------------------------
    # ZUSAMMENFASSUNG
    # ------------------------------------------------------------
    def update_summary(self):
        modus = "Einzelwert" if self.single_value_mode else "Gesamt"

        if self.single_value_mode:
            trenner = self.separator if self.separator is not None else "kein"
        else:
            trenner = "–"

        n_original = self.model.count_original_values()
        n_norm = self.model.count_norm_values()
        n_total = self.model.count_total_occurrences()

        self.ui.lbl_tag.setText(f"TAG: {self.tag}")
        self.ui.lbl_mode.setText(f"Modus: {modus}")
        self.ui.lbl_separator.setText(f"Trenner: {trenner}")

        self.ui.lbl_total_occ.setText(f"Vorkommen gesamt: {n_total}")
        self.ui.lbl_found_values.setText(f"Gefundene Werte: {n_original}")
        self.ui.lbl_norm_values.setText(f"Normwerte: {n_norm}")

    # ------------------------------------------------------------
    # ERSETZUNGSTABELLE
    # ------------------------------------------------------------
    def fill_replacements_table(self):
        table = self.ui.table_replacements

        table.setSortingEnabled(False)
        table.setRowCount(0)
        

        replacements = self.model.get_replacement_list()

        for row, (old, new, count) in enumerate(replacements):
            table.insertRow(row)

            # Spalte 0: neuer Wert
            item_new = TextItem(new)
            item_new.setFlags(item_new.flags() & ~Qt.ItemIsEditable)
            table.setItem(row, 0, item_new)

            # Spalte 1: alter Wert
            item_old = TextItem(old)
            item_old.setFlags(item_old.flags() & ~Qt.ItemIsEditable)
            table.setItem(row, 1, item_old)

            # Spalte 2: Anzahl
            item_count = NumericItem(str(count))
            item_count.setFlags(item_count.flags() & ~Qt.ItemIsEditable)
            table.setItem(row, 2, item_count)

        table.setSortingEnabled(True)
        self.apply_filter()

    # ------------------------------------------------------------
    # DATEI SCHREIBEN
    # ------------------------------------------------------------
    def on_write_clicked(self):
        if not self.original_path or not os.path.exists(self.original_path):
            QMessageBox.warning(self, "Fehler", "Die Eingabedatei existiert nicht mehr.")
            return

        base_dir = os.path.dirname(self.original_path)
        base_name = os.path.splitext(os.path.basename(self.original_path))[0]
        default_name = f"{base_name}_tidy_{self.tag}.ged"
        default_path = os.path.join(base_dir, default_name)

        out_path, _ = QFileDialog.getSaveFileName(
            self,
            "Bereinigte GEDCOM-Datei speichern",
            default_path,
            "GEDCOM-Dateien (*.ged);;Alle Dateien (*.*)"
        )
        if not out_path:
            return

        if os.path.abspath(out_path) == os.path.abspath(self.original_path):
            QMessageBox.warning(
                self,
                "Ungültiger Dateiname",
                "Die Ausgabedatei darf nicht identisch mit der Eingabedatei sein."
            )
            return

        self.output_path = out_path

        try:
            expected_replacements, actual_replacements = self._export_with_log()
        except Exception as e:
            QMessageBox.critical(self, "Fehler beim Export", str(e))
            return

        # Markdown-Vorschau aktualisieren
        try:
            log_path = self._logfile_path()
            if hasattr(self.ui, "md_preview"):
                with open(log_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.ui.md_preview.setMarkdown(content)
        except Exception:
            pass

        try:
            self.ui.tabWidget.setCurrentIndex(1)
        except Exception:
            pass

        if expected_replacements != actual_replacements:
            QMessageBox.warning(
                self,
                "Warnung",
                f"Es wurden {actual_replacements} von {expected_replacements} "
                f"erwarteten Ersetzungen durchgeführt.\n"
                f"Details siehe Logdatei."
            )

        QMessageBox.information(
            self,
            "Export abgeschlossen",
            (
                "Die bereinigte GEDCOM-Datei wurde erfolgreich erzeugt.\n\n"
                f"Die Protokolldatei wurde gespeichert unter:\n{self._logfile_path()}\n\n"
                "Sie können das Protokoll auch direkt im Programm einsehen."
            )
        )

    # ------------------------------------------------------------
    # EXPORT + LOG
    # ------------------------------------------------------------
    def _export_with_log(self):
        replacement_map = {old: new for old, new, _ in self.model.get_replacement_list()}

        expected_replacements = sum(
            count for _old, _new, count in self.model.get_replacement_list()
        )

        log_entries = []
        total_lines = 0
        total_replacements = 0
        current_pointer = ""

        mw = self._get_main_window()

        with open(self.original_path, "r", encoding="utf-8") as infile, \
             open(self.output_path, "w", encoding="utf-8", newline="") as outfile:

            for line_no, line in enumerate(infile, start=1):
                original_line = line.rstrip("\n")
                new_line = original_line

                ptr_match = re.match(r"0\s+@([^@]+)@", original_line)
                if ptr_match:
                    current_pointer = ptr_match.group(1)

                level, tag, value = self._parse_gedcom_line(original_line)

                if tag == self.tag and value is not None:
                    if self.single_value_mode and self.separator is not None:
                        new_value, replacements_here = self._replace_single_values(
                            value, replacement_map
                        )
                    else:
                        new_value, replacements_here = self._replace_full_value(
                            value, replacement_map
                        )

                    if replacements_here > 0:
                        new_line = self._rebuild_line(level, tag, new_value, original_line)
                        total_replacements += replacements_here
                        log_entries.append((line_no, current_pointer, original_line, new_line))

                outfile.write(new_line + "\n")
                total_lines += 1

                if total_lines % 100 == 0 and mw and hasattr(mw, "update_status"):
                    mw.update_status(f"Export läuft… {total_lines} Zeilen verarbeitet")

        self._write_logfile(
            total_lines,
            expected_replacements,
            total_replacements,
            log_entries
        )

        return expected_replacements, total_replacements

    # ------------------------------------------------------------
    # GEDCOM-Hilfsfunktionen
    # ------------------------------------------------------------
    def _parse_gedcom_line(self, line: str):
        parts = line.split(" ", 2)
        if len(parts) == 1:
            return parts[0], None, None
        if len(parts) == 2:
            return parts[0], parts[1], None
        level, tag, value = parts
        return level, tag, value

    def _rebuild_line(self, level: str, tag: str, value: str, original_line: str) -> str:
        m = re.match(r"^(\d+)(\s+)(\S+)(\s+)(.*)$", original_line)
        if m:
            lvl, space1, tg, space2, _old_val = m.groups()
            return f"{lvl}{space1}{tg}{space2}{value}"
        else:
            return f"{level} {tag} {value}"

    # ------------------------------------------------------------
    # ERSETZUNGEN
    # ------------------------------------------------------------
    def _replace_full_value(self, value: str, replacement_map: dict):
        if value in replacement_map:
            return replacement_map[value], 1
        return value, 0

    def _replace_single_values(self, value: str, replacement_map: dict):
        sep = self.separator
        if not sep:
            return self._replace_full_value(value, replacement_map)

        tokens = value.split(sep)
        new_tokens = []
        replacements_here = 0

        for token in tokens:
            if token in replacement_map:
                new_tokens.append(replacement_map[token])
                replacements_here += 1
            else:
                new_tokens.append(token)

        return sep.join(new_tokens), replacements_here

    # ------------------------------------------------------------
    # LOGDATEI
    # ------------------------------------------------------------
    def _logfile_path(self):
        base, _ = os.path.splitext(self.output_path)
        return base + "_log.md"

    def _write_logfile(
        self,
        total_lines: int,
        expected_replacements: int,
        actual_replacements: int,
        log_entries
    ):
        log_path = self._logfile_path()

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(log_path, "w", encoding="utf-8", newline="") as log:
            log.write(f"# Logdatei der GEDCOM‑Normalisierung (GedTidy {APP_VERSION})\n\n")
            log.write(f"**Erstellt:** {now}  \n")
            log.write(f"**Eingabedatei:** {self.original_path}  \n")
            log.write(f"**Ausgabedatei:** {self.output_path}  \n\n")

            log.write("## Statistik\n")
            log.write(f"- Gesamtzeilen: {total_lines}\n")
            log.write(f"- Erwartete Ersetzungen: {expected_replacements}\n")
            log.write(f"- Tatsächlich durchgeführte Ersetzungen: {actual_replacements}\n\n")

            modus = "Einzelwert" if self.single_value_mode else "Gesamt"
            sep_display = f"`{self.separator}`" if self.separator else "`kein`"

            log.write("## Einstellungen\n")
            log.write(f"- TAG: {self.tag}\n")
            log.write(f"- Modus: {modus}\n")
            log.write(f"- Trenner: {sep_display}\n\n")

            log.write("## Gefilterte Werte\n\n")
            log.write("| Normwert (neu) | TAG‑Wert (alt) | Vorkommen |\n")
            log.write("|----------------|----------------|-----------|\n")

            table = self.ui.table_replacements
            for row in range(table.rowCount()):
                if not table.isRowHidden(row):
                    new = table.item(row, 0).text()
                    old = table.item(row, 1).text()
                    count = table.item(row, 2).text()
                    log.write(f"| {new} | {old} | {count} |\n")

            log.write("\n")

            log.write("## Ersetzungen\n\n")
            log.write("| ged‑Zeile | Datensatz | Originalzeile | Neue Zeile |\n")
            log.write("|-----------|-----------|----------------|-------------|\n")

            for line_no, pointer, original, new in log_entries:
                o = original.replace("|", "\\|")
                n = new.replace("|", "\\|")
                p = (pointer or "").replace("|", "\\|")
                log.write(f"| {line_no} | {p} | `{o}` | `{n}` |\n")

    # ------------------------------------------------------------
    # FILTERFUNKTION
    # ------------------------------------------------------------
    def apply_filter(self):
        text = self.ui.edit_filter_replacements.text().lower()
        table = self.ui.table_replacements

        for row in range(table.rowCount()):
            old = table.item(row, 1).text().lower() if table.item(row, 1) else ""
            new = table.item(row, 0).text().lower() if table.item(row, 0) else ""
            count = table.item(row, 2).text().lower() if table.item(row, 2) else ""

            hide = (
                text not in old
                and text not in new
                and text not in count
            )
            table.setRowHidden(row, hide)

        self._update_filtered_sum_label()

    # ------------------------------------------------------------
    # SUMME GEFILTERTER ERSETZUNGEN
    # ------------------------------------------------------------
    def _update_filtered_sum_label(self):
        table = self.ui.table_replacements

        count_filtered = sum(
            1 for row in range(table.rowCount())
            if not table.isRowHidden(row)
        )
        self.ui.lbl_filtered_count.setText(f"Anzahl (gefiltert): {count_filtered}")

        total = 0
        for row in range(table.rowCount()):
            if not table.isRowHidden(row):
                item = table.item(row, 2)
                if item:
                    try:
                        total += int(item.text())
                    except ValueError:
                        pass

        self.ui.lbl_filtered_sum.setText(f"Ersetzungen (gefiltert): {total}")

    # ------------------------------------------------------------
    # MainWindow finden
    # ------------------------------------------------------------
    def _get_main_window(self):
        w = self.parent()
        while w is not None and not hasattr(w, "update_status"):
            w = w.parent()
        return w