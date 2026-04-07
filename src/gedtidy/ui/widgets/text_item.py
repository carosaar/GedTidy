from PySide6.QtWidgets import QTableWidgetItem

class TextItem(QTableWidgetItem):
    def __lt__(self, other):
        # Case-insensitive Vergleich
        if isinstance(other, QTableWidgetItem):
            return self.text().lower() < other.text().lower()
        return super().__lt__(other)