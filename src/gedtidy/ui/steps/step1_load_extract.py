"""
Step 1 – Load & Extract (Designer-Version)
"""

import os
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox,QApplication
from PySide6.QtCore import Qt, QThread


from gedtidy.ui.steps.step1_load_extract_ui import Ui_Step1_LoadAndExtract
from gedtidy.models.normalization_model import NormalizationModel
from gedtidy.ui.steps.step2_normalize import Step2_Normalize
from gedtidy.ui.widgets.numeric_item import NumericItem
from gedtidy.ui.workers.gedcom_worker import GedcomParserWorker
from gedtidy.ui.widgets.text_item import TextItem



SEARCH_TAGS = ["PLAC", "OCCU", "RELI", "CAUS", "TYPE", "SEX"]


class Step1_LoadAndExtract(QWidget):
    """
    Step 1 lädt die Designer-UI und enthält nur noch Logik.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Aktuelle Einstellungen
        self.current_tag = None
        self.current_single_value_mode = False
        self.current_separator = ", "

        # Designer-UI laden
        self.ui = Ui_Step1_LoadAndExtract()
        self.ui.setupUi(self)
        self.ui.combo_tags.clear()
        self.ui.combo_tags.addItems(SEARCH_TAGS)
        self.ui.combo_tags.setCurrentText("PLAC")
        self.ui.edit_filter.setClearButtonEnabled(True)


        # Daten
        self.rohdaten = []
        self.grouped_counts = {}
        self.step2_widget = None

        # Anfangszustand
        self.ui.stack_tables.setCurrentIndex(0)
        self.ui.label_summary_raw.hide()
        self.ui.edit_separator.setText(", ")


        # Signale verbinden
        self._connect_signals()

    # ---------------------------------------------------------
    # SIGNALVERBINDUNGEN
    # ---------------------------------------------------------
    def _connect_signals(self):
        self.ui.btn_select_file.clicked.connect(self.select_file)
        self.ui.btn_extract.clicked.connect(self.start_extraction)
        self.ui.btn_reset.clicked.connect(self.reset_all)

        self.ui.combo_view_mode.currentIndexChanged.connect(self.switch_view)
        self.ui.edit_filter.textChanged.connect(self.apply_filter)
        self.ui.edit_separator.textChanged.connect(self.update_separator_hint)

    # ---------------------------------------------------------
    # DATEI AUSWÄHLEN
    # ---------------------------------------------------------
    def select_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "GEDCOM-Datei wählen", "", "GEDCOM (*.ged);;Alle Dateien (*)"
        )
        if path:
            self.ui.edit_file.setText(path)
            self.ui.combo_tags.clear()
            self.ui.combo_tags.addItems(SEARCH_TAGS)

    # ---------------------------------------------------------
    # EXTRAKTION STARTEN
    # ---------------------------------------------------------
    def start_extraction(self):
        path = self.ui.edit_file.text().strip()
        if not path:
            QMessageBox.warning(self, "Fehler", "Bitte eine GEDCOM-Datei auswählen.")
            return

        if not os.path.exists(path):
            QMessageBox.warning(self, "Fehler", "Die Datei existiert nicht.")
            return

        tag = self.ui.combo_tags.currentText().strip()
        if tag not in SEARCH_TAGS:
            QMessageBox.warning(self, "Fehler", "Bitte einen gültigen TAG auswählen.")
            return

        if self.ui.chk_single_values.isChecked():
            separator = self.ui.edit_separator.text()

            # Leer oder nur Leerzeichen → echter Trenner ist ein Leerzeichen
            if separator == "" or separator.isspace():
                separator = " "
        else:
            separator = None

        # Aktuelle Einstellungen merken (für Export / Zustandsspeicherung)
        self.current_tag = tag
        self.current_single_value_mode = self.ui.chk_single_values.isChecked()
        self.current_separator = separator if separator is not None else ", "

        self._status("Extraktion läuft…")

        # Worker starten
        self.thread = QThread()
        self.worker = GedcomParserWorker(path, tag, separator, self.parse_gedcom)

        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)

        self.worker.finished.connect(self.on_parse_finished)
        self.worker.error.connect(self.on_parse_error)
        self.worker.progress.connect(self.on_parse_progress)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    # ---------------------------------------------------------
    # PARSER-CALLBACKS
    # ---------------------------------------------------------
    def on_parse_progress(self, percent):
        self._status(f"Extraktion läuft… {percent}%")

    def on_parse_error(self, message):
        QMessageBox.critical(self, "Parserfehler", message)
        self._status("Fehler bei der Extraktion.")

    def on_parse_finished(self, rohdaten):
        self.rohdaten = rohdaten

        # Tabellen aufbauen
        self.fill_tables_and_start_step2()

        # Abschlussmeldung
        self._status("Extraktion abgeschlossen.")

    # ---------------------------------------------------------
    # GEDCOM PARSER
    # ---------------------------------------------------------
    def parse_gedcom(self, path, tag, separator=None, progress_callback=None):
        rohdaten = []
        append = rohdaten.append
        current_pointer = None

        total_lines = sum(1 for _ in open(path, "r", encoding="utf-8"))

        with open(path, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                line = line.rstrip("\n")

                space1 = line.find(" ")
                if space1 == -1:
                    continue

                level = line[:space1]

                if level == "0":
                    space2 = line.find(" ", space1 + 1)
                    if space2 != -1:
                        token = line[space1+1 : space2].strip()
                        if token.startswith("@") and token.endswith("@"):
                            pointer_candidate = token[1:-1].strip()
                            if pointer_candidate and " " not in pointer_candidate:
                                current_pointer = pointer_candidate
                                continue

                space2 = line.find(" ", space1 + 1)
                if space2 == -1:
                    continue

                tagname = line[space1+1 : space2]

                if tagname != tag:
                    continue

                value = line[space2+1:] if len(line) > space2 else ""

                if separator:
                    for v in value.split(separator):
                        v = v.strip()
                        if v:
                            append({
                                "line": lineno,
                                "pointer": current_pointer,
                                "tag": tag,
                                "value": v,
                            })
                else:
                    if value:
                        append({
                            "line": lineno,
                            "pointer": current_pointer,
                            "tag": tag,
                            "value": value,
                        })

                if progress_callback and lineno % 500 == 0:
                    progress_callback.emit(int(lineno / total_lines * 100))

        return rohdaten

    # ---------------------------------------------------------
    # TABELLEN FÜLLEN + STEP2 STARTEN
    # ---------------------------------------------------------
    def fill_tables_and_start_step2(self):
        # ---------------------------------------------------------
        # 1) Sofortige Statusmeldung, bevor die lange Phase beginnt
        # ---------------------------------------------------------
        self._status("Tabellen werden aufgebaut…")

        # Qt zwingen, die Statusmeldung sofort zu zeichnen

        QApplication.processEvents()

        # ---------------------------------------------------------
        # 2) Gruppierte Werte berechnen (kann bei großen Dateien dauern)
        # ---------------------------------------------------------
        self.grouped_counts = {}
        for r in self.rohdaten:
            self.grouped_counts[r["value"]] = self.grouped_counts.get(r["value"], 0) + 1

        # ---------------------------------------------------------
        # 3) Tabellen aufbauen
        # ---------------------------------------------------------

        # Rohdaten
        table_r = self.ui.table_values_raw
        # table_r.setFocusPolicy(Qt.NoFocus)
        table_r.setStyleSheet("""
            QTableWidget::item:selected {
                background: transparent;
                color: black;
            }
        """)
        table_r.setSortingEnabled(False)
        table_r.verticalHeader().setVisible(False)
        table_r.setRowCount(0)

        for row, r in enumerate(self.rohdaten):
            table_r.insertRow(row)
            
            item = NumericItem(str(r["line"]))
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            table_r.setItem(row, 0, item)

            item = TextItem(r["pointer"] or "")
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            table_r.setItem(row, 1, item)

            item = TextItem(r["value"])
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            table_r.setItem(row, 2, item)

        table_r.setSortingEnabled(True)

        # Gruppierte Werte
        table_g = self.ui.table_values_grouped
        # table_g.setFocusPolicy(Qt.NoFocus)
        table_g.setStyleSheet("""
            QTableWidget::item:selected {
                background: transparent;
                color: black;
            }
        """)

        table_g.setSortingEnabled(False)
        table_g.verticalHeader().setVisible(False)
        table_g.setRowCount(0)

        for row, (value, count) in enumerate(sorted(self.grouped_counts.items())):
            table_g.insertRow(row)

            # Spalte 0: Wert
            item_value = TextItem(value)
            item_value.setFlags(item_value.flags() & ~Qt.ItemIsEditable)
            table_g.setItem(row, 0, item_value)

            # Spalte 1: Anzahl
            item_count = NumericItem(str(count))
            item_count.setFlags(item_count.flags() & ~Qt.ItemIsEditable)
            table_g.setItem(row, 1, item_count)

        table_g.setSortingEnabled(True)

        # Zusammenfassungen
        self.ui.label_summary_grouped.setText(
            f"Eindeutige Werte: {len(self.grouped_counts)}   Gesamtvorkommen: {len(self.rohdaten)}"
        )
        self.ui.label_summary_raw.setText(
            f"Rohdatensätze: {len(self.rohdaten)}"
        )

        self.apply_filter()

        # ---------------------------------------------------------
        # 4) Step2 erzeugen
        # ---------------------------------------------------------
        items = []
        for value, count in self.grouped_counts.items():
            items.append({
                "tag": value,
                "count": count,
                "is_selected": False,
                "is_norm": False,
                "norm_value": None
            })

        model = NormalizationModel(items)
        self.step2_widget = Step2_Normalize(model)

        # StepController finden
        controller = self.parent()
        while controller and not hasattr(controller, "set_step2"):
            controller = controller.parent()

        if controller is None:
            print("FEHLER: StepController nicht gefunden!")
            return

        controller.model = model
        controller.set_step2(self.step2_widget)

        # Navigation freischalten
        mw = controller.parent()
        if mw and hasattr(mw, "navigation"):
            mw.navigation.btn_step2.setEnabled(True)
            mw.navigation.btn_step3.setEnabled(True)

        # Einstellungen sperren
        self.ui.combo_tags.setEnabled(False)
        self.ui.chk_single_values.setEnabled(False)
        self.ui.edit_separator.setEnabled(False)
        self.ui.label_sep_hint.setEnabled(False)
        self.ui.btn_select_file.setEnabled(False)
        self.ui.edit_file.setEnabled(False)



    # ---------------------------------------------------------
    # ANSICHT WECHSELN
    # ---------------------------------------------------------
    def switch_view(self, index):
        self.ui.stack_tables.setCurrentIndex(index)
        self.apply_filter()

    # ---------------------------------------------------------
    # FILTER
    # ---------------------------------------------------------
    def apply_filter(self):
        text = self.ui.edit_filter.text().lower()

        # ---------------------------------------------------------
        # Gruppierte Werte
        # ---------------------------------------------------------
        table = self.ui.table_values_grouped
        for row in range(table.rowCount()):
            item_value = table.item(row, 0)
            item_count = table.item(row, 1)

            value = item_value.text().lower() if item_value else ""
            count = item_count.text().lower() if item_count else ""

            hide = (text not in value) and (text not in count)
            table.setRowHidden(row, hide)

        # ---------------------------------------------------------
        # Rohdaten
        # ---------------------------------------------------------
        table = self.ui.table_values_raw
        for row in range(table.rowCount()):
            item_line = table.item(row, 0)
            item_pointer = table.item(row, 1)
            item_value = table.item(row, 2)

            line = item_line.text().lower() if item_line else ""
            pointer = item_pointer.text().lower() if item_pointer else ""
            value = item_value.text().lower() if item_value else ""

            hide = (
                text not in line
                and text not in pointer
                and text not in value
            )
            table.setRowHidden(row, hide)

    # ---------------------------------------------------------
    # RESET
    # ---------------------------------------------------------
    def reset_all(self, silent=False):
        if not silent:
            reply = QMessageBox.question(
                self,
                "Reset bestätigen",
                "Soll wirklich ein kompletter Reset durchgeführt werden?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply != QMessageBox.Yes:
                return False

        # ---------------------------------------------------------
        # Step 1: Eigene UI zurücksetzen
        # ---------------------------------------------------------

        self.ui.edit_filter.clear()
        self.ui.edit_separator.setText(", ")
        self.ui.chk_single_values.setChecked(False)
        self.ui.label_sep_hint.hide()

        self.rohdaten = []
        self.grouped_counts = {}

        self.ui.table_values_grouped.setRowCount(0)
        self.ui.table_values_raw.setRowCount(0)

        self.ui.label_summary_grouped.setText("Noch keine Daten extrahiert.")
        self.ui.label_summary_raw.setText("Noch keine Rohdaten extrahiert.")

        self.step2_widget = None
        self.update_separator_hint()

        # Einstellungen wieder freischalten
        self.ui.combo_tags.setEnabled(True)
        self.ui.chk_single_values.setEnabled(True)
        self.ui.edit_separator.setEnabled(True)
        self.ui.label_sep_hint.setEnabled(True)
        self.ui.btn_select_file.setEnabled(True)
        self.ui.edit_file.setEnabled(True)

        # ---------------------------------------------------------
        # StepController + MainWindow korrekt ermitteln
        # ---------------------------------------------------------
        controller = self.parent()
        main_window = controller.parent() if controller else None

        # Statusunterdrückung aktivieren
        if main_window:
            main_window._suppress_status = True

        # StepController zurücksetzen
        if controller and hasattr(controller, "reset"):
            controller.reset()

        # Navigation zurücksetzen
        if main_window and hasattr(main_window, "navigation"):
            main_window.navigation.set_active(0)
            main_window.navigation.btn_step2.setEnabled(False)
            main_window.navigation.btn_step3.setEnabled(False)

        # Statusmeldung
        if main_window and hasattr(main_window, "update_status"):
            main_window.update_status("System zurückgesetzt – bitte neue Datei laden.")

        # Unterdrückung wieder deaktivieren
        if main_window:
            main_window._suppress_status = False

        return True
    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def _status(self, msg):
        # StepController finden (egal wie tief verschachtelt)
        controller = self.parent()
        while controller and not hasattr(controller, "update_status"):
            controller = controller.parent()

        # Import-Modus unterdrückt Step1-Statusmeldungen
        if hasattr(controller, "_import_mode") and controller._import_mode:
            return

        controller.update_status(msg)


    # ---------------------------------------------------------
    # SEPARATOR-HINWEIS
    # ---------------------------------------------------------

    def update_separator_hint(self):
        text = self.ui.edit_separator.text()

        # Wenn Feld leer ODER nur aus Leerzeichen besteht → Hinweis anzeigen
        if text == "" or text.isspace():
            self.ui.label_sep_hint.show()
        else:
            self.ui.label_sep_hint.hide()

        # Automatik: Nur einschalten, wenn der Trenner NICHT der Default ist
        # und der Einzelwerte-Modus noch aus ist.
        if text != ", " and not self.ui.chk_single_values.isChecked():
            self.ui.chk_single_values.setChecked(True)

    # ---------------------------------------------------------
    # IMPORT-EINSTELLUNGEN ÜBERNEHMEN   
    # ---------------------------------------------------------
    def apply_import_settings(self, source_file, tag, single_value_mode, separator):
        """Übernimmt Einstellungen aus dem Import, ohne sie zu überschreiben."""

        # Datei setzen
        self.ui.edit_file.setText(source_file)

        # TAG setzen
        self.ui.combo_tags.setCurrentText(tag)

        # Modus setzen
        self.ui.chk_single_values.setChecked(single_value_mode)

        # Separator setzen
        if separator:
            self.ui.edit_separator.setText(separator)
        else:
            self.ui.edit_separator.setText(", ")

        # interne Variablen setzen
        self.current_tag = tag
        self.current_single_value_mode = single_value_mode
        self.current_separator = separator if separator else ", "
    

        # Hinweis aktualisieren
        self.update_separator_hint()