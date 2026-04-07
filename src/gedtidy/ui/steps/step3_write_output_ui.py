# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'step3_write_output.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Step3_WriteOutput(object):
    def setupUi(self, Step3_WriteOutput):
        if not Step3_WriteOutput.objectName():
            Step3_WriteOutput.setObjectName(u"Step3_WriteOutput")
        Step3_WriteOutput.resize(461, 742)
        self.mainLayout = QVBoxLayout(Step3_WriteOutput)
        self.mainLayout.setSpacing(14)
        self.mainLayout.setObjectName(u"mainLayout")
        self.frame_summary = QFrame(Step3_WriteOutput)
        self.frame_summary.setObjectName(u"frame_summary")
        self.summaryGrid = QGridLayout(self.frame_summary)
        self.summaryGrid.setObjectName(u"summaryGrid")
        self.lbl_head_inputs = QLabel(self.frame_summary)
        self.lbl_head_inputs.setObjectName(u"lbl_head_inputs")

        self.summaryGrid.addWidget(self.lbl_head_inputs, 0, 0, 1, 1)

        self.lbl_tag = QLabel(self.frame_summary)
        self.lbl_tag.setObjectName(u"lbl_tag")

        self.summaryGrid.addWidget(self.lbl_tag, 1, 0, 1, 1)

        self.lbl_mode = QLabel(self.frame_summary)
        self.lbl_mode.setObjectName(u"lbl_mode")

        self.summaryGrid.addWidget(self.lbl_mode, 2, 0, 1, 1)

        self.lbl_separator = QLabel(self.frame_summary)
        self.lbl_separator.setObjectName(u"lbl_separator")

        self.summaryGrid.addWidget(self.lbl_separator, 3, 0, 1, 1)

        self.lbl_head_stats = QLabel(self.frame_summary)
        self.lbl_head_stats.setObjectName(u"lbl_head_stats")

        self.summaryGrid.addWidget(self.lbl_head_stats, 0, 1, 1, 1)

        self.lbl_total_occ = QLabel(self.frame_summary)
        self.lbl_total_occ.setObjectName(u"lbl_total_occ")

        self.summaryGrid.addWidget(self.lbl_total_occ, 1, 1, 1, 1)

        self.lbl_found_values = QLabel(self.frame_summary)
        self.lbl_found_values.setObjectName(u"lbl_found_values")

        self.summaryGrid.addWidget(self.lbl_found_values, 2, 1, 1, 1)

        self.lbl_head_norm = QLabel(self.frame_summary)
        self.lbl_head_norm.setObjectName(u"lbl_head_norm")

        self.summaryGrid.addWidget(self.lbl_head_norm, 0, 2, 1, 1)

        self.lbl_norm_values = QLabel(self.frame_summary)
        self.lbl_norm_values.setObjectName(u"lbl_norm_values")

        self.summaryGrid.addWidget(self.lbl_norm_values, 1, 2, 1, 1)


        self.mainLayout.addWidget(self.frame_summary)

        self.tabWidget = QTabWidget(Step3_WriteOutput)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_preview = QWidget()
        self.tab_preview.setObjectName(u"tab_preview")
        self.previewLayout = QVBoxLayout(self.tab_preview)
        self.previewLayout.setObjectName(u"previewLayout")
        self.group_replacements = QGroupBox(self.tab_preview)
        self.group_replacements.setObjectName(u"group_replacements")
        self.tableLayout = QVBoxLayout(self.group_replacements)
        self.tableLayout.setObjectName(u"tableLayout")
        self.edit_filter_replacements = QLineEdit(self.group_replacements)
        self.edit_filter_replacements.setObjectName(u"edit_filter_replacements")

        self.tableLayout.addWidget(self.edit_filter_replacements)

        self.table_replacements = QTableWidget(self.group_replacements)
        if (self.table_replacements.columnCount() < 3):
            self.table_replacements.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_replacements.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_replacements.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_replacements.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_replacements.setObjectName(u"table_replacements")
        self.table_replacements.setAlternatingRowColors(True)
        self.table_replacements.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_replacements.setSortingEnabled(True)

        self.tableLayout.addWidget(self.table_replacements)

        self.table_sumLayout = QHBoxLayout()
        self.table_sumLayout.setObjectName(u"table_sumLayout")
        self.lbl_filtered_count = QLabel(self.group_replacements)
        self.lbl_filtered_count.setObjectName(u"lbl_filtered_count")

        self.table_sumLayout.addWidget(self.lbl_filtered_count)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.table_sumLayout.addItem(self.horizontalSpacer)

        self.lbl_filtered_sum = QLabel(self.group_replacements)
        self.lbl_filtered_sum.setObjectName(u"lbl_filtered_sum")

        self.table_sumLayout.addWidget(self.lbl_filtered_sum)


        self.tableLayout.addLayout(self.table_sumLayout)


        self.previewLayout.addWidget(self.group_replacements)

        self.tabWidget.addTab(self.tab_preview, "")
        self.tab_log = QWidget()
        self.tab_log.setObjectName(u"tab_log")
        self.vboxLayout = QVBoxLayout(self.tab_log)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.md_preview = QTextBrowser(self.tab_log)
        self.md_preview.setObjectName(u"md_preview")
        self.md_preview.setMinimumSize(QSize(0, 200))
        self.md_preview.setOpenExternalLinks(True)

        self.vboxLayout.addWidget(self.md_preview)

        self.tabWidget.addTab(self.tab_log, "")

        self.mainLayout.addWidget(self.tabWidget)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.buttonSpacer)

        self.btn_write = QPushButton(Step3_WriteOutput)
        self.btn_write.setObjectName(u"btn_write")
        self.btn_write.setStyleSheet(u"\n"
"         QPushButton {\n"
"           background-color: #2a7ade;\n"
"           color: white;\n"
"           font-size: 12pt;\n"
"           font-weight: bold;\n"
"           border-radius: 6px;\n"
"           padding: 6px 12px;\n"
"         }\n"
"         QPushButton:hover {\n"
"           background-color: #1f5fb1;\n"
"         }\n"
"        ")

        self.buttonLayout.addWidget(self.btn_write)


        self.mainLayout.addLayout(self.buttonLayout)


        self.retranslateUi(Step3_WriteOutput)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Step3_WriteOutput)
    # setupUi

    def retranslateUi(self, Step3_WriteOutput):
        Step3_WriteOutput.setWindowTitle(QCoreApplication.translate("Step3_WriteOutput", u"Step 3 \u2013 Bereinigte Datei erzeugen", None))
        self.frame_summary.setStyleSheet(QCoreApplication.translate("Step3_WriteOutput", u"\n"
"        QFrame#frame_summary {\n"
"          background-color: #f7f9fc;\n"
"          border: 1px solid #d0d7e2;\n"
"          border-radius: 6px;\n"
"          padding: 12px;\n"
"        }\n"
"        QLabel {\n"
"          font-size: 10pt;\n"
"          color: #2a3f5f;\n"
"        }\n"
"        QLabel.heading {\n"
"          font-weight: bold;\n"
"          font-size: 11pt;\n"
"        }\n"
"      ", None))
        self.lbl_head_inputs.setStyleSheet(QCoreApplication.translate("Step3_WriteOutput", u"font-weight: bold;", None))
        self.lbl_head_inputs.setText(QCoreApplication.translate("Step3_WriteOutput", u"Vorgaben", None))
        self.lbl_tag.setText(QCoreApplication.translate("Step3_WriteOutput", u"TAG:", None))
        self.lbl_mode.setText(QCoreApplication.translate("Step3_WriteOutput", u"Modus:", None))
        self.lbl_separator.setText(QCoreApplication.translate("Step3_WriteOutput", u"Trenner:", None))
        self.lbl_head_stats.setStyleSheet(QCoreApplication.translate("Step3_WriteOutput", u"font-weight: bold;", None))
        self.lbl_head_stats.setText(QCoreApplication.translate("Step3_WriteOutput", u"Statistik", None))
        self.lbl_total_occ.setText(QCoreApplication.translate("Step3_WriteOutput", u"Vorkommen gesamt:", None))
        self.lbl_found_values.setText(QCoreApplication.translate("Step3_WriteOutput", u"Gefundene Werte:", None))
        self.lbl_head_norm.setStyleSheet(QCoreApplication.translate("Step3_WriteOutput", u"font-weight: bold;", None))
        self.lbl_head_norm.setText(QCoreApplication.translate("Step3_WriteOutput", u"Normierung", None))
        self.lbl_norm_values.setText(QCoreApplication.translate("Step3_WriteOutput", u"Normwerte:", None))
        self.group_replacements.setTitle(QCoreApplication.translate("Step3_WriteOutput", u"\U0001f504 Ersetzungstabelle", None))
        self.edit_filter_replacements.setPlaceholderText(QCoreApplication.translate("Step3_WriteOutput", u"\U0001f50d Filtern\U00002026", None))
        ___qtablewidgetitem = self.table_replacements.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Step3_WriteOutput", u"Normwert (neu)", None))
        ___qtablewidgetitem1 = self.table_replacements.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Step3_WriteOutput", u"TAG\u2011Wert (alt)", None))
        ___qtablewidgetitem2 = self.table_replacements.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Step3_WriteOutput", u"Vorkommen", None))
        self.lbl_filtered_count.setText(QCoreApplication.translate("Step3_WriteOutput", u"Anzahl (gefiltert): 0", None))
        self.lbl_filtered_sum.setText(QCoreApplication.translate("Step3_WriteOutput", u"Ersetzungen (gefiltert): 0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_preview), QCoreApplication.translate("Step3_WriteOutput", u"Vorschau", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_log), QCoreApplication.translate("Step3_WriteOutput", u"Protokoll", None))
        self.btn_write.setText(QCoreApplication.translate("Step3_WriteOutput", u"\U0001f4e4 Bereinigte Datei erzeugen", None))
    # retranslateUi

