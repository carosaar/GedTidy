from PySide6.QtWidgets import QWidget, QMessageBox, QAbstractItemView, QHeaderView
from PySide6.QtCore import Qt, QTimer, QSortFilterProxyModel
from PySide6.QtGui import QStandardItemModel, QStandardItem

from gedtidy.models.normalization_model import NormalizationModel
from gedtidy.ui.steps.step2_normalize_ui import Ui_Step2_NormalizeUI


class Step2_Normalize(QWidget):
    """
    Designer-basierte Version von Step 2.
    Stabil: keine Crashes bei Filter, Navigation, Löschen, Editieren.
    """

    def __init__(self, model: NormalizationModel, parent=None):
        super().__init__(parent)

        self.model = model
        self._suppress_norm_edit = False

        # Designer-UI laden
        self.ui = Ui_Step2_NormalizeUI()
        self.ui.setupUi(self)

        # ---------------------------------------------------------
        # Linke Tabelle
        # ---------------------------------------------------------
        self.table_left = self.ui.table_left
        self.model_left = QStandardItemModel(self)
        self.proxy_left = QSortFilterProxyModel(self)
        self.proxy_left.setSourceModel(self.model_left)
        self.proxy_left.setSortCaseSensitivity(Qt.CaseInsensitive)

        self.table_left.setModel(self.proxy_left)
        self._init_left_header()
        self.table_left.verticalHeader().setVisible(False)

        header = self.table_left.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        header.setSectionResizeMode(1, QHeaderView.Interactive)
        header.setSectionResizeMode(2, QHeaderView.Interactive)
        header.setSectionResizeMode(3, QHeaderView.Fixed)

        header.resizeSection(0, 30)
        header.resizeSection(1, 250)
        header.resizeSection(2, 38)
        header.resizeSection(3, 40)

        self.model_left.itemChanged.connect(self.on_left_item_changed)

        # self.table_left.setFocusPolicy(Qt.NoFocus)
        self.table_left.setStyleSheet("""
            QTableView::item:selected {
                background: transparent;
                color: black;
            }
        """)


        # ---------------------------------------------------------
        # Mittlere Tabelle (Normwerte)
        # ---------------------------------------------------------
        self.table_norm = self.ui.table_norm
        self.model_norm = QStandardItemModel(self)
        self.proxy_norm = QSortFilterProxyModel(self)
        self.proxy_norm.setSourceModel(self.model_norm)
        self.proxy_norm.setSortCaseSensitivity(Qt.CaseInsensitive)

        self.table_norm.setModel(self.proxy_norm)
        self._init_norm_header()
        self.table_norm.verticalHeader().setVisible(False)
        self.table_norm.setEditTriggers(QAbstractItemView.EditKeyPressed)

        header = self.table_norm.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Interactive)
        header.setSectionResizeMode(1, QHeaderView.Interactive)
        header.setSectionResizeMode(2, QHeaderView.Interactive)

        header.resizeSection(0, 270)
        header.resizeSection(1, 40)
        header.resizeSection(2, 40)

        # self.table_left.setFocusPolicy(Qt.NoFocus)
        self.table_left.setStyleSheet("""
            QTableView::item:selected {
                background: transparent;
                color: black;
            }
        """)

        # ---------------------------------------------------------
        # Rechte Tabelle (Details)
        # ---------------------------------------------------------
        self.table_details = self.ui.table_details
        self.model_details = QStandardItemModel(self)
        self.proxy_details = QSortFilterProxyModel(self)
        self.proxy_details.setSourceModel(self.model_details)
        self.proxy_details.setSortCaseSensitivity(Qt.CaseInsensitive)

        self.table_details.setModel(self.proxy_details)
        self._init_details_header()
        self.table_details.verticalHeader().setVisible(False)

        header = self.table_details.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Interactive)
        header.setSectionResizeMode(1, QHeaderView.Interactive)

        header.resizeSection(0, 300)
        header.resizeSection(1, 40)

        # self.table_left.setFocusPolicy(Qt.NoFocus)
        self.table_left.setStyleSheet("""
            QTableView::item:selected {
                background: transparent;
                color: black;
            }
        """)

        # Filter
        self.filter_left = self.ui.filter_left
        self.filter_norm = self.ui.filter_norm
        self.filter_details = self.ui.filter_details

        # Buttons
        self.btn_assign = self.ui.btn_assign
        self.btn_delete_single_norm = self.ui.btn_delete_single_norm
        self.btn_delete_norm_list = self.ui.btn_delete_norm_list
        self.btn_delete_details = self.ui.btn_delete_details

        # Signale verbinden
        self._connect_signals()

        # Initiales Rendering
        self.refresh_all()

    # ---------------------------------------------------------
    # SIGNALVERBINDUNGEN
    # ---------------------------------------------------------
    def _connect_signals(self):
        # Filter
        self.filter_left.textChanged.connect(self.on_filter_left)
        self.filter_norm.textChanged.connect(self.on_filter_norm)
        self.filter_details.textChanged.connect(self.on_filter_details)

        # Tabellen
        self.table_left.doubleClicked.connect(self.on_left_doubleclick)
        self.table_left.clicked.connect(self.on_left_cell_clicked)

        self.table_norm.clicked.connect(self.on_norm_clicked)
        self.table_norm.doubleClicked.connect(self.on_norm_doubleclick)
        self.model_norm.itemChanged.connect(self.on_norm_edited)
        self.table_norm.selectionModel().currentChanged.connect(self.on_norm_current_changed)

        self.table_details.doubleClicked.connect(self.on_details_doubleclick)

        # Sortierung
        self.table_left.setSortingEnabled(True)
        self.table_norm.setSortingEnabled(True)
        self.table_details.setSortingEnabled(True)

        # Buttons
        self.btn_assign.clicked.connect(self.assign_selected)
        self.btn_delete_single_norm.clicked.connect(self.delete_single_norm)
        self.btn_delete_norm_list.clicked.connect(self.delete_all_norms)
        self.btn_delete_details.clicked.connect(self.delete_all_details)

    # ---------------------------------------------------------
    # FILTER
    # ---------------------------------------------------------
    def on_filter_left(self, text):
        self.model.filter_left = text
        self.refresh_left()

    def on_filter_norm(self, text):
        self.model.filter_norm = text
        self.refresh_norm()

    def on_filter_details(self, text):
        self.model.filter_details = text
        self.refresh_details()

    # ---------------------------------------------------------
    # REFRESH
    # ---------------------------------------------------------
    def refresh_all(self):
        self.refresh_left()
        self.refresh_norm()
        self.refresh_details()

    # ---------------------------------------------------------
    # LINKES FENSTER
    # ---------------------------------------------------------
    def refresh_left(self):
        items = self.model.get_left_items()

        proxy_row = self.table_left.currentIndex().row()

        self.table_left.setSortingEnabled(False)
        self.model_left.setRowCount(0)

        for item in items:
            row_items = []

            # Spalte 0: Checkbox
            chk_item = QStandardItem()
            chk_item.setCheckable(True)
            chk_item.setFlags(chk_item.flags() & ~Qt.ItemIsEditable)
            chk_item.setCheckState(Qt.Checked if item.get("is_selected") else Qt.Unchecked)
            chk_item.setData(item["tag"], Qt.UserRole)
            row_items.append(chk_item)

            # Spalte 1: TAG-Wert
            tag_item = QStandardItem(f"• {item['tag']}")
            tag_item.setData(item["tag"], Qt.UserRole)
            tag_item.setFlags(tag_item.flags() & ~Qt.ItemIsEditable)
            row_items.append(tag_item)

            # Spalte 2: Anzahl
            count_item = QStandardItem(str(item["count"]))
            count_item.setData(item["count"], Qt.EditRole)
            count_item.setFlags(count_item.flags() & ~Qt.ItemIsEditable)
            row_items.append(count_item)

            # Spalte 3: Normwert-Markierung
            norm_item = QStandardItem("🔖" if item["norm_value"] is None else "")
            norm_item.setTextAlignment(Qt.AlignCenter)
            norm_item.setFlags(norm_item.flags() & ~Qt.ItemIsEditable)
            row_items.append(norm_item)

            self.model_left.appendRow(row_items)

        self.table_left.setSortingEnabled(True)

        if self.model_left.rowCount() == 0:
            return

        if proxy_row < 0:
            proxy_row = 0
        if proxy_row >= self.proxy_left.rowCount():
            proxy_row = self.proxy_left.rowCount() - 1

        index = self.proxy_left.index(proxy_row, 0)
        self.table_left.setCurrentIndex(index)

    # ---------------------------------------------------------
    # MITTLERE TABELLE
    # ---------------------------------------------------------
    def refresh_norm(self):
        norms = self.model.get_norm_values()

        self.table_norm.setSortingEnabled(False)
        self.model_norm.setRowCount(0)

        for n in norms:
            row_items = []

            pure = n["norm"]
            is_current = (self.model.current_norm == pure)

            display = f"⭐ {pure}" if is_current else f"🏷️ {pure}"
            item_norm = QStandardItem(display)
            item_norm.setData(pure, Qt.UserRole)
            item_norm.setEditable(True)

            if is_current:
                font = item_norm.font()
                font.setBold(True)
                item_norm.setFont(font)
                item_norm.setForeground(Qt.red)

            row_items.append(item_norm)

            count_item = QStandardItem(str(n["count_items"]))
            count_item.setEditable(False)
            row_items.append(count_item)

            sum_item = QStandardItem(str(n["sum_counts"]))
            sum_item.setEditable(False)
            row_items.append(sum_item)

            self.model_norm.appendRow(row_items)

        self.table_norm.setSortingEnabled(True)

        # Auswahl / current_norm nach Filter / Änderungen
        row_count = self.model_norm.rowCount()
        if row_count == 0:
            self.model.current_norm = None
            self.refresh_details()
            return

        # Versuchen, current_norm wiederzufinden
        found_row = None
        for row in range(row_count):
            item = self.model_norm.item(row, 0)
            if item is None:
                continue
            pure = item.data(Qt.UserRole)
            if pure == self.model.current_norm:
                found_row = row
                break

        if found_row is not None:
            source_index = self.model_norm.index(found_row, 0)
            proxy_index = self.proxy_norm.mapFromSource(source_index)
            self.table_norm.setCurrentIndex(proxy_index)
        else:
            # ersten Eintrag aktiv setzen
            source_index = self.model_norm.index(0, 0)
            proxy_index = self.proxy_norm.mapFromSource(source_index)
            self.table_norm.setCurrentIndex(proxy_index)
            new_norm = self.model_norm.item(0, 0).data(Qt.UserRole)
            self.model.select_norm(new_norm)

        self.refresh_details()

    # ---------------------------------------------------------
    # RECHTES FENSTER
    # ---------------------------------------------------------
    def refresh_details(self):
        items = self.model.get_details_for_current_norm()

        proxy_row = self.table_details.currentIndex().row()

        self.table_details.setSortingEnabled(False)
        self.model_details.setRowCount(0)

        for item in items:
            row_items = []

            tag_item = QStandardItem(f"• {item['tag']}")
            tag_item.setData(item["tag"], Qt.UserRole)
            tag_item.setEditable(False)
            row_items.append(tag_item)

            count_item = QStandardItem(str(item["count"]))
            count_item.setEditable(False)
            row_items.append(count_item)

            self.model_details.appendRow(row_items)

        self.table_details.setSortingEnabled(True)

        if self.model_details.rowCount() > 0:
            if proxy_row < 0:
                proxy_row = 0
            if proxy_row >= self.proxy_details.rowCount():
                proxy_row = self.proxy_details.rowCount() - 1

            index = self.proxy_details.index(proxy_row, 0)
            self.table_details.setCurrentIndex(index)

    # ---------------------------------------------------------
    # AKTIONEN
    # ---------------------------------------------------------
    def assign_selected(self):
        selected = [
            item["tag"]
            for item in self.model.items
            if item["is_selected"] and item["norm_value"] is None
        ]
        self.model.assign_to_current_norm(selected)

        for item in self.model.items:
            item["is_selected"] = False

        self.refresh_all()

    def on_left_doubleclick(self, index):
        if not index.isValid():
            return

        proxy_index = index.sibling(index.row(), 1)
        source_index = self.proxy_left.mapToSource(proxy_index)
        if not source_index.isValid():
            return

        item = self.model_left.item(source_index.row(), 1)
        if item is None:
            return

        tag = item.data(Qt.UserRole)
        self.model.assign_single(tag)
        self.refresh_all()

    def on_left_cell_clicked(self, index):
        if not index.isValid():
            return
        if index.column() != 3:
            return

        proxy_index = index.sibling(index.row(), 1)
        source_index = self.proxy_left.mapToSource(proxy_index)
        if not source_index.isValid():
            return

        item = self.model_left.item(source_index.row(), 1)
        if item is None:
            return

        tag = item.data(Qt.UserRole)
        self.model.set_norm_value(tag)
        self.refresh_all()

    # ---------------------------------------------------------
    # MITTE: Klick / Tastatur / Doppelklick
    # ---------------------------------------------------------
    def on_norm_clicked(self, index):
        if not index.isValid():
            return

        # index ist ein Proxy-Index → auf Spalte 0 umbiegen
        proxy_index = index.sibling(index.row(), 0)

        # Proxy → Source mappen
        source_index = self.proxy_norm.mapToSource(proxy_index)
        if not source_index.isValid():
            return

        item = self.model_norm.item(source_index.row(), 0)
        if item is None:
            return

        norm = item.data(Qt.UserRole)
        if not norm:
            return

        self.model.select_norm(norm)
        self.refresh_norm()
        self.refresh_details()

    def on_norm_current_changed(self, current, previous):
        if self.proxy_norm.rowCount() == 0:
            return
        if not current.isValid():
            return

        proxy_index = current.sibling(current.row(), 0)
        source_index = self.proxy_norm.mapToSource(proxy_index)
        if not source_index.isValid():
            return

        item = self.model_norm.item(source_index.row(), 0)
        if item is None:
            return

        norm = item.data(Qt.UserRole)
        if not norm:
            return

        self.model.select_norm(norm)
        self.table_norm.setCurrentIndex(current)
        self.refresh_details()

        # Hervorhebung aktualisieren
        for row in range(self.model_norm.rowCount()):
            it = self.model_norm.item(row, 0)
            if it is None:
                continue
            pure = it.data(Qt.UserRole)
            is_current = (pure == self.model.current_norm)

            display = f"⭐ {pure}" if is_current else f"🏷️ {pure}"
            it.setText(display)

            font = it.font()
            font.setBold(is_current)
            it.setFont(font)
            it.setForeground(Qt.red if is_current else Qt.black)

    def on_norm_doubleclick(self, index):
        if not index.isValid():
            return

        proxy_index = index.sibling(index.row(), 0)
        source_index = self.proxy_norm.mapToSource(proxy_index)
        if not source_index.isValid():
            return

        item = self.model_norm.item(source_index.row(), 0)
        if item is None:
            return

        norm_to_delete = item.data(Qt.UserRole)
        if not norm_to_delete:
            return

        self._suppress_norm_edit = True
        self.model.delete_norm_value(norm_to_delete)
        self._suppress_norm_edit = False

        norms = self.model.get_norm_values()
        if norms:
            source_row = source_index.row()
            if source_row < len(norms):
                new_norm = norms[source_row]["norm"]
            else:
                new_norm = norms[-1]["norm"]
            self.model.select_norm(new_norm)
        else:
            self.model.current_norm = None

        self.refresh_norm()
        self.refresh_details()
        self.table_norm.setFocus()

    # ---------------------------------------------------------
    # RECHTS: Doppelklick
    # ---------------------------------------------------------
    def on_details_doubleclick(self, index):
        if not index.isValid():
            return

        proxy_index = index.sibling(index.row(), 0)
        source_index = self.proxy_details.mapToSource(proxy_index)
        if not source_index.isValid():
            return

        item = self.model_details.item(source_index.row(), 0)
        if item is None:
            return

        tag = item.data(Qt.UserRole)
        self.model.remove_detail(tag)
        self.refresh_all()

    # ---------------------------------------------------------
    # LÖSCH-BUTTONS
    # ---------------------------------------------------------
    def delete_all_details(self):
        if not self.model.current_norm:
            return

        norm = self.model.current_norm

        reply = QMessageBox.question(
            self,
            "Detailwerte löschen",
            f"Sollen wirklich alle Detailwerte des Normwerts\n„{norm}“ gelöscht werden?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return

        details = self.model.get_details_for_current_norm()
        for item in details:
            item["norm_value"] = None
            item["is_selected"] = False

        self.model.delete_norm_value(norm)
        self.model.current_norm = None

        self.refresh_all()

    def delete_single_norm(self):
        if not self.model.current_norm:
            QMessageBox.warning(
                self,
                "Kein Normwert ausgewählt",
                "Bitte wählen Sie zuerst einen Normwert aus.",
            )
            return

        norm = self.model.current_norm

        reply = QMessageBox.question(
            self,
            "Normwert löschen",
            f"Soll der Normwert „{norm}“ wirklich gelöscht werden?\n"
            "Alle zugehörigen Detailwerte werden zurück in die linke Liste verschoben.",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return

        self.model.delete_norm_value(norm)
        self.refresh_all()
        self.table_norm.setFocus()

    def delete_all_norms(self):
        reply = QMessageBox.question(
            self,
            "Alle Normwerte löschen",
            "Sollen wirklich alle Normwerte gelöscht werden?\n"
            "Alle zugewiesenen Detailwerte werden zurück in die linke Liste verschoben.",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return

        self.model.delete_all_norms()
        self.refresh_all()
        self.table_norm.setFocus()

    # ---------------------------------------------------------
    # EDIT NORMWERT
    # ---------------------------------------------------------
    def on_norm_edited(self, item):
        if self._suppress_norm_edit:
            return
        if item.column() != 0:
            return

        raw = item.text().strip()

        if raw.startswith("⭐ ") or raw.startswith("🏷️ "):
            new_value = raw[2:].strip()
        else:
            new_value = raw

        if not new_value:
            old = self.model.current_norm
            self.model.delete_norm_value(old)
            QTimer.singleShot(0, self.refresh_all)
            return

        old_value = item.data(Qt.UserRole)
        if new_value == old_value:
            return

        self.model.rename_norm_value(old_value, new_value)
        QTimer.singleShot(0, self.refresh_all)

    # ---------------------------------------------------------
    # HEADER-INITIALISIERUNG
    # ---------------------------------------------------------
    def _init_left_header(self):
        self.model_left.setColumnCount(4)
        self.model_left.setHorizontalHeaderLabels(["", "Wert", "N°", "Norm"])

    def _init_norm_header(self):
        self.model_norm.setColumnCount(3)
        self.model_norm.setHorizontalHeaderLabels(["Normwert", "N°", "Σ"])

    def _init_details_header(self):
        self.model_details.setColumnCount(2)
        self.model_details.setHorizontalHeaderLabels(["TAG‑Wert", "N°"])

    # ---------------------------------------------------------
    # CHECKBOX-ÄNDERUNGEN LINKS
    # ---------------------------------------------------------
    def on_left_item_changed(self, item):
        if item.column() != 0:
            return

        tag = item.data(Qt.UserRole)
        checked = item.checkState() == Qt.Checked
        model_item = self.model._get_item(tag)
        if model_item:
            model_item["is_selected"] = checked


    # ---------------------------------------------------------
    # REFRESH-METHODEN
    # ---------------------------------------------------------
    def refresh(self):
        """UI neu aufbauen, nachdem das Model geändert wurde."""
        self.refresh_all()  