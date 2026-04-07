from PySide6.QtWidgets import QMainWindow, QMessageBox
from gedtidy.ui.main_window_ui import Ui_MainWindow
from PySide6.QtGui import QPixmap

from gedtidy.ui.widgets.navigation_panel import NavigationPanel
from gedtidy.ui.widgets.step_controller import StepController
from gedtidy.version import APP_VERSION

from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, icon_path):
        super().__init__()

        self.icon_path = icon_path
        
        # Fenster-Titel mit Version setzen
        self.setWindowTitle(f"GedTidy {APP_VERSION}")
        self.setWindowIcon(QIcon(str(icon_path)))

        # UI laden
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Fenster-Titel mit Version setzen
        self.setWindowTitle(f"GedTidy {APP_VERSION}")


        # Status-Unterdrückung (wird z.B. beim Reset genutzt)
        self._suppress_status = False

        # Statusleiste initialisieren
        self.statusBar().showMessage("Bereit.")

        # Navigation links
        self.navigation = NavigationPanel()
        self.ui.navLayout.addWidget(self.navigation)

        # StepController erzeugen und in Layout einfügen
        self.step_controller = StepController(self)
        self.ui.stepLayout.addWidget(self.step_controller)

        # Navigation verbinden
        self.navigation.btn_step0.clicked.connect(lambda: self.goto_step(0))
        self.navigation.btn_step2.clicked.connect(lambda: self.goto_step(1))
        self.navigation.btn_step3.clicked.connect(lambda: self.goto_step(2))

        # Menüaktionen verbinden
        self._connect_menu_actions()

    # ---------------------------------------------------------
    # Menüaktionen
    # ---------------------------------------------------------
    def _connect_menu_actions(self):
        # Laden
        self.ui.action_load_state.triggered.connect(
            lambda: self.step_controller.import_state()
        )

        # Speichern
        self.ui.action_save_state.triggered.connect(
            lambda: self.step_controller.export_state()
        )

        # Speichern unter... (kannst du später entfernen, wenn immer Dialog)
        self.ui.action_save_state_as.triggered.connect(
            lambda: self.step_controller.export_state(save_as=True)
        )

        # Info
        self.ui.action_info.triggered.connect(self.show_info_dialog)

        # Beenden
        self.ui.action_exit.triggered.connect(self.close)

    # ---------------------------------------------------------
    # Navigation
    # ---------------------------------------------------------
    def goto_step(self, index: int):
        self.step_controller.go_to(index)

    # ---------------------------------------------------------
    # Info-Dialog
    # ---------------------------------------------------------
    def show_info_dialog(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Über GedTidy")

        # HTML-Text wie bisher
        msg.setText(
            f"<b>GedTidy – {APP_VERSION}</b><br><br>"
            "Ein Werkzeug zur Analyse und Normalisierung genealogischer GEDCOM‑Daten.<br>"
            "Für Anwenderinnen und Anwender, die mit GEDCOM‑Dateien arbeiten.<br><br>"
            "Alle Daten werden ausschließlich lokal auf dem eigenen Computer verarbeitet.<br><br>"
            "Entwickelt mit Python und PySide6.<br>"
            "Betriebssystem: Microsoft Windows 10/11.<br><br>"
            "Lizenz: MIT License<br>"
            '<a href="https://github.com/carosaar">https://github.com/carosaar</a><br><br>'
            "© 2026 Dieter Eckstein"
        )

        # eigenes Icon einbinden
        msg.setIconPixmap(QPixmap(str(self.icon_path)).scaled(64, 64))

        msg.exec()


    # ---------------------------------------------------------
    # Statusmeldung
    # ---------------------------------------------------------
    def update_status(self, msg: str):
        """
        Wird von Step1 / StepController aufgerufen, um eine Statusmeldung
        in der Statusleiste anzuzeigen.
        """
        if self._suppress_status:
            return
        self.statusBar().showMessage(msg)