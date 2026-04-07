"""
GedTidy - Navigation Panel

Modernisierte Navigation mit Step-Buttons und Unicode-Symbolen.
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from gedtidy.ui.widgets.navigation_panel_ui import Ui_NavigationPanel

class NavigationPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NavigationPanel()
        self.ui.setupUi(self)

        self.btn_step0 = self.ui.btn_step0
        self.btn_step2 = self.ui.btn_step2
        self.btn_step3 = self.ui.btn_step3

    # ---------------------------------------------------------
    # Aktiven Schritt visuell markieren
    # ---------------------------------------------------------
    def set_active(self, index: int):
        self.btn_step0.setChecked(index == 0)
        self.btn_step2.setChecked(index == 1)
        self.btn_step3.setChecked(index == 2)