# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'step1_load_extract.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Step1_LoadAndExtract(object):
    def setupUi(self, Step1_LoadAndExtract):
        if not Step1_LoadAndExtract.objectName():
            Step1_LoadAndExtract.setObjectName(u"Step1_LoadAndExtract")
        Step1_LoadAndExtract.resize(1200, 700)
        self.mainLayout = QHBoxLayout(Step1_LoadAndExtract)
        self.mainLayout.setObjectName(u"mainLayout")
        self.group_settings = QGroupBox(Step1_LoadAndExtract)
        self.group_settings.setObjectName(u"group_settings")
        self.settingsLayout = QVBoxLayout(self.group_settings)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.fileLayout = QHBoxLayout()
        self.fileLayout.setObjectName(u"fileLayout")
        self.edit_file = QLineEdit(self.group_settings)
        self.edit_file.setObjectName(u"edit_file")

        self.fileLayout.addWidget(self.edit_file)

        self.btn_select_file = QPushButton(self.group_settings)
        self.btn_select_file.setObjectName(u"btn_select_file")

        self.fileLayout.addWidget(self.btn_select_file)


        self.settingsLayout.addLayout(self.fileLayout)

        self.tagLayout = QHBoxLayout()
        self.tagLayout.setObjectName(u"tagLayout")
        self.label_tag = QLabel(self.group_settings)
        self.label_tag.setObjectName(u"label_tag")

        self.tagLayout.addWidget(self.label_tag)

        self.combo_tags = QComboBox(self.group_settings)
        self.combo_tags.setObjectName(u"combo_tags")
        self.combo_tags.setMinimumSize(QSize(200, 0))

        self.tagLayout.addWidget(self.combo_tags)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.tagLayout.addItem(self.horizontalSpacer_4)


        self.settingsLayout.addLayout(self.tagLayout)

        self.sepLayout = QHBoxLayout()
        self.sepLayout.setObjectName(u"sepLayout")
        self.chk_single_values = QCheckBox(self.group_settings)
        self.chk_single_values.setObjectName(u"chk_single_values")

        self.sepLayout.addWidget(self.chk_single_values)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.sepLayout.addItem(self.horizontalSpacer_6)

        self.label_sep = QLabel(self.group_settings)
        self.label_sep.setObjectName(u"label_sep")

        self.sepLayout.addWidget(self.label_sep)

        self.edit_separator = QLineEdit(self.group_settings)
        self.edit_separator.setObjectName(u"edit_separator")
        self.edit_separator.setMinimumSize(QSize(100, 0))

        self.sepLayout.addWidget(self.edit_separator)

        self.label_sep_hint = QLabel(self.group_settings)
        self.label_sep_hint.setObjectName(u"label_sep_hint")
        self.label_sep_hint.setVisible(False)

        self.sepLayout.addWidget(self.label_sep_hint)


        self.settingsLayout.addLayout(self.sepLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.settingsLayout.addItem(self.verticalSpacer)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer_2)

        self.btn_extract = QPushButton(self.group_settings)
        self.btn_extract.setObjectName(u"btn_extract")
        self.btn_extract.setMinimumSize(QSize(180, 60))
        self.btn_extract.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.btn_extract.setFont(font)
        self.btn_extract.setIconSize(QSize(16, 16))
        self.btn_extract.setFlat(False)

        self.buttonLayout.addWidget(self.btn_extract)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.btn_reset = QPushButton(self.group_settings)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMinimumSize(QSize(180, 60))
        self.btn_reset.setFont(font)

        self.buttonLayout.addWidget(self.btn_reset)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer_3)


        self.settingsLayout.addLayout(self.buttonLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.settingsLayout.addItem(self.verticalSpacer_2)


        self.mainLayout.addWidget(self.group_settings)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.setObjectName(u"rightLayout")
        self.filterLayout = QHBoxLayout()
        self.filterLayout.setObjectName(u"filterLayout")
        self.label_view = QLabel(Step1_LoadAndExtract)
        self.label_view.setObjectName(u"label_view")

        self.filterLayout.addWidget(self.label_view)

        self.combo_view_mode = QComboBox(Step1_LoadAndExtract)
        self.combo_view_mode.addItem("")
        self.combo_view_mode.addItem("")
        self.combo_view_mode.setObjectName(u"combo_view_mode")

        self.filterLayout.addWidget(self.combo_view_mode)

        self.filterSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.filterLayout.addItem(self.filterSpacer)

        self.label_filter = QLabel(Step1_LoadAndExtract)
        self.label_filter.setObjectName(u"label_filter")

        self.filterLayout.addWidget(self.label_filter)

        self.edit_filter = QLineEdit(Step1_LoadAndExtract)
        self.edit_filter.setObjectName(u"edit_filter")

        self.filterLayout.addWidget(self.edit_filter)


        self.rightLayout.addLayout(self.filterLayout)

        self.label_summary_grouped = QLabel(Step1_LoadAndExtract)
        self.label_summary_grouped.setObjectName(u"label_summary_grouped")

        self.rightLayout.addWidget(self.label_summary_grouped)

        self.label_summary_raw = QLabel(Step1_LoadAndExtract)
        self.label_summary_raw.setObjectName(u"label_summary_raw")

        self.rightLayout.addWidget(self.label_summary_raw)

        self.stack_tables = QStackedWidget(Step1_LoadAndExtract)
        self.stack_tables.setObjectName(u"stack_tables")
        self.page_grouped = QWidget()
        self.page_grouped.setObjectName(u"page_grouped")
        self.layout_grouped = QVBoxLayout(self.page_grouped)
        self.layout_grouped.setObjectName(u"layout_grouped")
        self.table_values_grouped = QTableWidget(self.page_grouped)
        if (self.table_values_grouped.columnCount() < 2):
            self.table_values_grouped.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_values_grouped.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_values_grouped.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_values_grouped.setObjectName(u"table_values_grouped")
        self.table_values_grouped.setColumnCount(2)

        self.layout_grouped.addWidget(self.table_values_grouped)

        self.stack_tables.addWidget(self.page_grouped)
        self.page_raw = QWidget()
        self.page_raw.setObjectName(u"page_raw")
        self.layout_raw = QVBoxLayout(self.page_raw)
        self.layout_raw.setObjectName(u"layout_raw")
        self.table_values_raw = QTableWidget(self.page_raw)
        if (self.table_values_raw.columnCount() < 3):
            self.table_values_raw.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_values_raw.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_values_raw.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_values_raw.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.table_values_raw.setObjectName(u"table_values_raw")
        self.table_values_raw.setColumnCount(3)

        self.layout_raw.addWidget(self.table_values_raw)

        self.stack_tables.addWidget(self.page_raw)

        self.rightLayout.addWidget(self.stack_tables)


        self.mainLayout.addLayout(self.rightLayout)


        self.retranslateUi(Step1_LoadAndExtract)

        QMetaObject.connectSlotsByName(Step1_LoadAndExtract)
    # setupUi

    def retranslateUi(self, Step1_LoadAndExtract):
        Step1_LoadAndExtract.setWindowTitle(QCoreApplication.translate("Step1_LoadAndExtract", u"Step 1 - Load and Extract", None))
        self.group_settings.setTitle(QCoreApplication.translate("Step1_LoadAndExtract", u"Einstellungen", None))
        self.btn_select_file.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Datei...", None))
        self.label_tag.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"TAG:", None))
        self.chk_single_values.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Einzelwerte extrahieren", None))
        self.label_sep.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Trenner:", None))
        self.edit_separator.setText(QCoreApplication.translate("Step1_LoadAndExtract", u", ", None))
        self.label_sep_hint.setStyleSheet(QCoreApplication.translate("Step1_LoadAndExtract", u"color: gray; font-size: 10px;", None))
        self.label_sep_hint.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Leerzeichen", None))
        self.btn_extract.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"\U0001f50d Extrahieren", None))
        self.btn_reset.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"\U0001f504 Reset", None))
        self.label_view.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Ansicht:", None))
        self.combo_view_mode.setItemText(0, QCoreApplication.translate("Step1_LoadAndExtract", u"Gruppierte Werte", None))
        self.combo_view_mode.setItemText(1, QCoreApplication.translate("Step1_LoadAndExtract", u"Rohdaten", None))

        self.label_filter.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Filter:", None))
        self.label_summary_grouped.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Noch keine Daten extrahiert.", None))
        self.label_summary_raw.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Noch keine Rohdaten extrahiert.", None))
        ___qtablewidgetitem = self.table_values_grouped.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Wert", None))
        ___qtablewidgetitem1 = self.table_values_grouped.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Vorkommen", None))
        ___qtablewidgetitem2 = self.table_values_raw.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Zeile", None))
        ___qtablewidgetitem3 = self.table_values_raw.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Pointer", None))
        ___qtablewidgetitem4 = self.table_values_raw.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Step1_LoadAndExtract", u"Wert", None))
    # retranslateUi

