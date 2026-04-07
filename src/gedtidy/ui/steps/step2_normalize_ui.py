# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'step2_normalize.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_Step2_NormalizeUI(object):
    def setupUi(self, Step2_NormalizeUI):
        if not Step2_NormalizeUI.objectName():
            Step2_NormalizeUI.setObjectName(u"Step2_NormalizeUI")
        Step2_NormalizeUI.resize(1400, 800)
        self.mainLayout = QHBoxLayout(Step2_NormalizeUI)
        self.mainLayout.setObjectName(u"mainLayout")
        self.group_left = QGroupBox(Step2_NormalizeUI)
        self.group_left.setObjectName(u"group_left")
        self.leftLayout = QVBoxLayout(self.group_left)
        self.leftLayout.setObjectName(u"leftLayout")
        self.filter_left = QLineEdit(self.group_left)
        self.filter_left.setObjectName(u"filter_left")

        self.leftLayout.addWidget(self.filter_left)

        self.table_left = QTableView(self.group_left)
        self.table_left.setObjectName(u"table_left")

        self.leftLayout.addWidget(self.table_left)

        self.btn_assign = QPushButton(self.group_left)
        self.btn_assign.setObjectName(u"btn_assign")

        self.leftLayout.addWidget(self.btn_assign)


        self.mainLayout.addWidget(self.group_left)

        self.group_norm = QGroupBox(Step2_NormalizeUI)
        self.group_norm.setObjectName(u"group_norm")
        self.midLayout = QVBoxLayout(self.group_norm)
        self.midLayout.setObjectName(u"midLayout")
        self.filter_norm = QLineEdit(self.group_norm)
        self.filter_norm.setObjectName(u"filter_norm")

        self.midLayout.addWidget(self.filter_norm)

        self.table_norm = QTableView(self.group_norm)
        self.table_norm.setObjectName(u"table_norm")

        self.midLayout.addWidget(self.table_norm)

        self.normButtons = QHBoxLayout()
        self.normButtons.setObjectName(u"normButtons")
        self.btn_delete_single_norm = QPushButton(self.group_norm)
        self.btn_delete_single_norm.setObjectName(u"btn_delete_single_norm")

        self.normButtons.addWidget(self.btn_delete_single_norm)

        self.btn_delete_norm_list = QPushButton(self.group_norm)
        self.btn_delete_norm_list.setObjectName(u"btn_delete_norm_list")

        self.normButtons.addWidget(self.btn_delete_norm_list)

        self.normSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.normButtons.addItem(self.normSpacer)


        self.midLayout.addLayout(self.normButtons)


        self.mainLayout.addWidget(self.group_norm)

        self.group_details = QGroupBox(Step2_NormalizeUI)
        self.group_details.setObjectName(u"group_details")
        self.rightLayout = QVBoxLayout(self.group_details)
        self.rightLayout.setObjectName(u"rightLayout")
        self.filter_details = QLineEdit(self.group_details)
        self.filter_details.setObjectName(u"filter_details")

        self.rightLayout.addWidget(self.filter_details)

        self.table_details = QTableView(self.group_details)
        self.table_details.setObjectName(u"table_details")

        self.rightLayout.addWidget(self.table_details)

        self.btn_delete_details = QPushButton(self.group_details)
        self.btn_delete_details.setObjectName(u"btn_delete_details")

        self.rightLayout.addWidget(self.btn_delete_details)


        self.mainLayout.addWidget(self.group_details)


        self.retranslateUi(Step2_NormalizeUI)

        QMetaObject.connectSlotsByName(Step2_NormalizeUI)
    # setupUi

    def retranslateUi(self, Step2_NormalizeUI):
        self.group_left.setTitle(QCoreApplication.translate("Step2_NormalizeUI", u"TAG\u2011Werte (Detailwerte)", None))
        self.filter_left.setPlaceholderText(QCoreApplication.translate("Step2_NormalizeUI", u"Filter\u2026", None))
        self.btn_assign.setText(QCoreApplication.translate("Step2_NormalizeUI", u">>", None))
        self.group_norm.setTitle(QCoreApplication.translate("Step2_NormalizeUI", u"Normwerte", None))
        self.filter_norm.setPlaceholderText(QCoreApplication.translate("Step2_NormalizeUI", u"Filter\u2026", None))
        self.btn_delete_single_norm.setText(QCoreApplication.translate("Step2_NormalizeUI", u"Normwert l\u00f6schen", None))
        self.btn_delete_norm_list.setText(QCoreApplication.translate("Step2_NormalizeUI", u"Zur\u00fccksetzen", None))
        self.group_details.setTitle(QCoreApplication.translate("Step2_NormalizeUI", u"Detailwerte des Normwerts", None))
        self.filter_details.setPlaceholderText(QCoreApplication.translate("Step2_NormalizeUI", u"Filter\u2026", None))
        self.btn_delete_details.setText(QCoreApplication.translate("Step2_NormalizeUI", u"Detailwerte l\u00f6schen", None))
        pass
    # retranslateUi

