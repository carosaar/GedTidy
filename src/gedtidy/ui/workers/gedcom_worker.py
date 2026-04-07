# ui/workers/gedcom_worker.py

from PySide6.QtCore import QObject, Signal

class GedcomParserWorker(QObject):
    finished = Signal(list)
    progress = Signal(int)
    error = Signal(str)

    def __init__(self, path, tag, separator, parser_func):
        super().__init__()
        self.path = path
        self.tag = tag
        self.separator = separator
        self.parser_func = parser_func

    def run(self):
        try:
            rohdaten = self.parser_func(
                self.path,
                self.tag,
                self.separator,
                self.progress     # <-- WICHTIG!
            )
            self.finished.emit(rohdaten)
        except Exception as e:
            self.error.emit(str(e))