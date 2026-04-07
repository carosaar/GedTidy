"""
GedTidy - Main Entry Point

Dieses Script startet die GedTidy-Anwendung.
"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from gedtidy.ui.main_window import MainWindow

from pathlib import Path


def main():
    app = QApplication(sys.argv)

    # Icon liegt im Projekt-Root unter /assets/
    
    if getattr(sys, 'frozen', False):
        # EXE-Modus
        base_path = Path(sys._MEIPASS)
    else:
        # Entwicklungsmodus
        base_path = Path(__file__).resolve().parents[2]

    icon_path = base_path / "assets" / "gedtidy.ico"

    # Debug-Ausgaben zum Icon-Pfad
    # print("Icon path:", icon_path)
    # print("Icon exists:", icon_path.exists())

    app.setWindowIcon(QIcon(str(icon_path)))

    window = MainWindow(icon_path)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()