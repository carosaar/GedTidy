# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'navigation_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_NavigationPanel(object):
    def setupUi(self, NavigationPanel):
        if not NavigationPanel.objectName():
            NavigationPanel.setObjectName(u"NavigationPanel")
        NavigationPanel.resize(211, 400)
        NavigationPanel.setStyleSheet(u"\n"
"QPushButton {\n"
"    text-align: left;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 6px;\n"
"    background-color: #f7f7f7;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #e8e8e8;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #d0e6ff;\n"
"    border: 1px solid #5aa0ff;\n"
"    font-weight: bold;\n"
"}\n"
"   ")
        self.verticalLayout = QVBoxLayout(NavigationPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_step0 = QPushButton(NavigationPanel)
        self.btn_step0.setObjectName(u"btn_step0")
        self.btn_step0.setMaximumSize(QSize(16777215, 16777215))
        self.btn_step0.setCheckable(True)

        self.verticalLayout.addWidget(self.btn_step0)

        self.btn_step2 = QPushButton(NavigationPanel)
        self.btn_step2.setObjectName(u"btn_step2")
        self.btn_step2.setMaximumSize(QSize(16777215, 16777215))
        self.btn_step2.setCheckable(False)

        self.verticalLayout.addWidget(self.btn_step2)

        self.btn_step3 = QPushButton(NavigationPanel)
        self.btn_step3.setObjectName(u"btn_step3")
        self.btn_step3.setMaximumSize(QSize(16777215, 16777215))
        self.btn_step3.setCheckable(False)

        self.verticalLayout.addWidget(self.btn_step3)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(NavigationPanel)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(180, 16777215))
        self.label.setFrameShape(QFrame.Shape.Box)
        self.label.setFrameShadow(QFrame.Shadow.Raised)
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(NavigationPanel)

        QMetaObject.connectSlotsByName(NavigationPanel)
    # setupUi

    def retranslateUi(self, NavigationPanel):
        NavigationPanel.setWindowTitle(QCoreApplication.translate("NavigationPanel", u"NavigationPanel", None))
        self.btn_step0.setText(QCoreApplication.translate("NavigationPanel", u"\U0001f9f0  Vorbereitung", None))
        self.btn_step2.setText(QCoreApplication.translate("NavigationPanel", u"\U0001f6e0\U0000fe0f  Normierung", None))
        self.btn_step3.setText(QCoreApplication.translate("NavigationPanel", u"\U0001f4dd  GED schreiben", None))
        self.label.setText(QCoreApplication.translate("NavigationPanel", u"<b><h2>\U0001f4a1 Hinweis:</H2></b><br>\n"
"Die erzeugte ged-Datei kann anschlie\U000000dfend in Ihr Genealogie-programm importiert werden.<br><br>Es empfiehlt sich, die Original- <b>und</b> die Protokolldatei als <b>Sicherung</b> aufzubewahren.<br", None))
    # retranslateUi

