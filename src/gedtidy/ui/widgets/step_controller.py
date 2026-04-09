"""
GedTidy - Step Controller
"""

from PySide6.QtWidgets import (
    QStackedWidget, QWidget, QFileDialog, QMessageBox,
    QDialog, QVBoxLayout, QListWidget, QPushButton, QApplication
)

from gedtidy.ui.steps.step1_load_extract import Step1_LoadAndExtract
from gedtidy.ui.steps.step2_normalize import Step2_Normalize
from gedtidy.ui.steps.step3_write_output import Step3_WriteOutput
from gedtidy.models.normalization_model import NormalizationModel
import json
from datetime import datetime
import os


class StepController(QStackedWidget):
    """
    Verwaltet Step1, Step2 und Step3.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.model = None
        self._import_mode = False

        # Step1 immer vorhanden
        self.step1 = Step1_LoadAndExtract(self)
        self.addWidget(self.step1)  # Index 0

        # Platzhalter für Step2/3
        self.step2 = QWidget()
        self.step3 = QWidget()
        self.addWidget(self.step2)  # Index 1
        self.addWidget(self.step3)  # Index 2

    # ============================================================
    # STEP 2 SETZEN
    # ============================================================
    def set_step2(self, widget: Step2_Normalize):
        if hasattr(widget, "model"):
            self.model = widget.model

        old = self.widget(1)
        if old:
            self.removeWidget(old)
            old.deleteLater()

        self.insertWidget(1, widget)
        self.step2 = widget

    # ============================================================
    # STEP 3 SETZEN
    # ============================================================
    def set_step3(self):
        if self.model is None or not isinstance(self.step2, Step2_Normalize):
            return

        old = self.widget(2)
        if old:
            self.removeWidget(old)
            old.deleteLater()

        new_step3 = Step3_WriteOutput(
            model=self.model,
            rohdaten=self.step1.rohdaten,
            tag=self.step1.current_tag,
            original_path=self.step1.ui.edit_file.text(),
            separator=self.step1.current_separator
                if self.step1.current_single_value_mode else None,
            single_value_mode=self.step1.current_single_value_mode,
            parent=self
        )

        self.insertWidget(2, new_step3)
        self.step3 = new_step3

    # ============================================================
    # NAVIGATION
    # ============================================================
    def go_to(self, index: int):
        if index == 1 and not isinstance(self.step2, Step2_Normalize):
            return

        if index == 2:
            if self.model is None:
                return
            self.set_step3()

        self.setCurrentIndex(index)

    # ============================================================
    # RESET
    # ============================================================
    def reset(self):
        if self.step2:
            self.removeWidget(self.step2)
            self.step2.deleteLater()
        self.step2 = QWidget()
        self.insertWidget(1, self.step2)

        if self.step3:
            self.removeWidget(self.step3)
            self.step3.deleteLater()
        self.step3 = QWidget()
        self.insertWidget(2, self.step3)

        self.model = None
        self.setCurrentIndex(0)

    # ============================================================
    # EXPORT
    # ============================================================
    def export_state(self, save_as=False):
        if self.model is None:
            QMessageBox.warning(None, "Kein Arbeitsstand",
                                "Es gibt keinen Arbeitsstand, der gespeichert werden kann.")
            return

        norms = [
            {"value": item["tag"], "norm": item["norm_value"]}
            for item in self.model.items
            if item["norm_value"] is not None
        ]

        data = {
            "version": 1,
            "saved_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "source_file": self.step1.ui.edit_file.text().strip(),
            "tag": self.step1.current_tag,
            "single_value_mode": self.step1.current_single_value_mode,
            "separator": self.step1.current_separator,
            "norms": norms
        }

        
        # Basisname der GEDCOM-Datei ermitteln und Standardname für Arbeitsstand vorschlagen
        ged_path = self.step1.ui.edit_file.text().strip()
        tag = self.step1.current_tag or "TAG"

        if ged_path:
            base = os.path.splitext(os.path.basename(ged_path))[0]
            default_name = f"{base}_{tag}.tidy"   #<-- z.B. "meine_stammbaumdatei_PLAC.tidy"
            default_path = os.path.join(os.path.dirname(ged_path), default_name)
        else:
            default_path = f"arbeitsstand_{tag}.tidy"    

        path, _ = QFileDialog.getSaveFileName(
            None,
            "Arbeitsstand speichern",
            default_path,
            "GedTidy-Arbeitsstand (*.tidy)"
        )

        if not path:
            return
        if not path.lower().endswith(".tidy"):
            path += ".tidy"

        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            QMessageBox.information(None, "Gespeichert",
                                    f"Arbeitsstand wurde gespeichert:\n{path}")

        except Exception as e:
            QMessageBox.critical(None, "Fehler beim Speichern", str(e))

    # ============================================================
    # IMPORT
    # ============================================================
    def import_state(self):
        """
        Lädt einen gespeicherten Arbeitsstand (.tidy) und bereitet
        den Import vor. Die eigentliche Übernahme passiert erst nach
        Bestätigung im Dialog.
        """
        self._import_mode = True

        # Datei auswählen
        path, _ = QFileDialog.getOpenFileName(
            None, "Arbeitsstand laden", "", "GedTidy-Arbeitsstand (*.tidy)"
        )
        if not path:
            self._import_mode = False
            return

        # JSON laden
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            QMessageBox.critical(None, "Fehler beim Laden", str(e))
            self._import_mode = False
            return

        # Pflichtfelder prüfen
        required = ["source_file", "tag", "single_value_mode", "separator", "norms"]
        for key in required:
            if key not in data:
                QMessageBox.critical(
                    None, "Ungültige Datei",
                    f"Die Datei enthält kein gültiges Arbeitsstandsformat.\nFehlend: {key}"
                )
                self._import_mode = False
                return

        source_file = data["source_file"]
        tag = data["tag"]
        single_value_mode = data["single_value_mode"]
        separator = data["separator"]
        saved_norms = data["norms"]
        saved_at = data.get("saved_at", "unbekannt")

        # GEDCOM prüfen
        if not os.path.exists(source_file):
            QMessageBox.critical(
                None, "Quelldatei fehlt",
                f"Die ursprüngliche GEDCOM-Datei existiert nicht mehr:\n{source_file}"
            )
            self._import_mode = False
            return

        # MainWindow sicher finden
        mw = self.parent()
        while mw and not hasattr(mw, "update_status"):
            mw = mw.parent()

        if mw:
            update_status = mw.update_status
        else:
            update_status = lambda msg: None

        # ---------------------------------------------------------
        # Statusmeldung SOFORT anzeigen
        # ---------------------------------------------------------
        update_status("Arbeitsstand wird vorbereitet…")

        # Qt zwingen, die Meldung sofort zu zeichnen
        
        QApplication.processEvents()

        # ---------------------------------------------------------
        # GEDCOM parsen (ohne UI!)
        # ---------------------------------------------------------
        rohdaten = self.step1.parse_gedcom(
            source_file,
            tag,
            separator if single_value_mode else None
        )

        # Gruppierte Werte berechnen
        grouped = {}
        for r in rohdaten:
            grouped[r["value"]] = grouped.get(r["value"], 0) + 1

        # Vorschau-Join
        missing, applied, missing_values = self._preview_norms(saved_norms, grouped)
        self._missing_values = missing_values

        # ---------------------------------------------------------
        # Statusmeldung löschen, bevor der Dialog erscheint
        # ---------------------------------------------------------
        update_status("")

        ged_path = source_file
        ged_name = os.path.basename(source_file)


        # Läuft aktuell eine Normierung?
        has_norm = isinstance(self.step2, Step2_Normalize) or self.model is not None

        # Hinweistext für evtl. laufende Normierung
        reset_hint = ""
        if has_norm:
            reset_hint = (
                "\n\nHinweis: Der aktuelle Arbeitsstand (Normierung) wird verworfen "
                "und durch den gespeicherten Arbeitsstand ersetzt."
            )

        # Vorbereitung abgeschlossen
        update_status("Arbeitsstand geprüft – bitte Auswahl im Dialog treffen.")

        while True:
            msg = QMessageBox()
            msg.setWindowTitle("Arbeitsstand geladen")
            msg.setIcon(QMessageBox.Information)

            # FALL 1: Keine Abweichungen
            if missing == 0:
                msg.setText(
                    f"GEDCOM-Datei:\n{ged_path}\n"
                    f"Arbeitsstand vom {saved_at} wurde geladen.\n\n"
                    f"Übernommene Normierungen: {applied}\n"
                    f"Keine Abweichungen gefunden.{reset_hint}\n\n"
                    "Möchten Sie den Import übernehmen?"
                )
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg.setDefaultButton(QMessageBox.Yes)

                result = msg.exec()

                if result == QMessageBox.Yes:
                    self._apply_import(
                        source_file, tag, single_value_mode, separator,
                        rohdaten, saved_norms
                    )
                    update_status("Import erfolgreich übernommen.")
                else:
                    update_status("Import abgebrochen.")

                self._import_mode = False
                return

            # FALL 2: Abweichungen vorhanden
            msg.setText(
                f"GEDCOM-Datei:\n{ged_path}\n"
                f"Arbeitsstand vom {saved_at} wurde geladen.\n\n"
                f"Übernommene Normierungen: {applied}\n"
                f"Die Datei „{ged_name}“ hat sich geändert.\n"
                f"Es fehlen {missing} Werte aus dem gespeicherten Arbeitsstand."
                f"{reset_hint}\n\n"
                "Möchten Sie den Import übernehmen?"
            )

            btn_yes = msg.addButton("Ja", QMessageBox.YesRole)
            btn_no = msg.addButton("Nein", QMessageBox.NoRole)
            btn_show = msg.addButton("Fehlende Werte anzeigen", QMessageBox.ActionRole)

            msg.setDefaultButton(btn_yes)
            msg.exec()

            if msg.clickedButton() == btn_yes:
                self._apply_import(
                    source_file, tag, single_value_mode, separator,
                    rohdaten, saved_norms
                )
                update_status("Import erfolgreich übernommen.")
                self._import_mode = False
                return

            if msg.clickedButton() == btn_no:
                update_status("Import abgebrochen.")
                self._import_mode = False
                return

            if msg.clickedButton() == btn_show:
                self._show_missing_values_dialog(self._missing_values)
                continue

    # ============================================================
    # Vorschau-Join (ohne Model)
    # ============================================================
    def _preview_norms(self, saved_norms, grouped):
        saved_map = {e["value"]: e["norm"] for e in saved_norms}

        current_values = set(grouped.keys())

        applied = sum(1 for v in current_values if v in saved_map)

        missing_values = [
            {"value": v, "norm": saved_map[v]}
            for v in saved_map
            if v not in current_values
        ]

        return len(missing_values), applied, missing_values

    # ============================================================
    # Import wirklich übernehmen
    # ============================================================
    def _apply_import(self, source_file, tag, single_value_mode, separator,
                      rohdaten, saved_norms):

        # Reset nur wenn Normierung läuft
        has_norm = isinstance(self.step2, Step2_Normalize) or self.model is not None
        if has_norm:
            if not self.step1.reset_all(silent=True):
                return

        # Step1 UI setzen
        self.step1.apply_import_settings(
            source_file, tag, single_value_mode, separator
        )

        # Rohdaten übernehmen
        self.step1.rohdaten = rohdaten

        # Tabellen + Model erzeugen
        self.step1.fill_tables_and_start_step2()

        # Normen anwenden
        missing, applied = self._apply_saved_norms(saved_norms)

        if isinstance(self.step2, Step2_Normalize):
            self.step2.refresh()

    # ============================================================
    # Normen anwenden (mit Model)
    # ============================================================
    def _apply_saved_norms(self, saved_norms):
        self._missing_values = []

        saved_map = {e["value"]: e["norm"] for e in saved_norms}

        applied = 0
        current_values = {item["tag"] for item in self.model.items}

        for item in self.model.items:
            if item["tag"] in saved_map:
                item["norm_value"] = saved_map[item["tag"]]
                applied += 1

        for v, norm in saved_map.items():
            if v not in current_values:
                self._missing_values.append({"value": v, "norm": norm})

        return len(self._missing_values), applied

    # ============================================================
    # Dialog fehlende Werte
    # ============================================================
    def _show_missing_values_dialog(self, values):
        dlg = QDialog()
        dlg.setWindowTitle("Fehlende Werte")

        layout = QVBoxLayout(dlg)
        listw = QListWidget()

        for entry in values:
            listw.addItem(f"{entry['value']}  →  {entry['norm']}")

        layout.addWidget(listw)

        btn_close = QPushButton("Zurück")
        btn_close.clicked.connect(dlg.accept)
        layout.addWidget(btn_close)

        dlg.exec()