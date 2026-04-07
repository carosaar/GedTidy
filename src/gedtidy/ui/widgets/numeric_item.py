from PySide6.QtWidgets import QTableWidgetItem

class NumericItem(QTableWidgetItem):
    """
    Ein QTableWidgetItem, das numerisch sortiert.
    """

    def __lt__(self, other):
        try:
            return float(self.text()) < float(other.text())
        except ValueError:
            return self.text() < other.text()