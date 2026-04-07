# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 800)
        self.action_load_state = QAction(MainWindow)
        self.action_load_state.setObjectName(u"action_load_state")
        self.action_save_state = QAction(MainWindow)
        self.action_save_state.setObjectName(u"action_save_state")
        self.action_save_state_as = QAction(MainWindow)
        self.action_save_state_as.setObjectName(u"action_save_state_as")
        self.action_info = QAction(MainWindow)
        self.action_info.setObjectName(u"action_info")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.separator = QAction(MainWindow)
        self.separator.setObjectName(u"separator")
        self.separator.setProperty(u"separator", True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.navLayout = QVBoxLayout()
        self.navLayout.setObjectName(u"navLayout")

        self.horizontalLayout.addLayout(self.navLayout)

        self.stepLayout = QVBoxLayout()
        self.stepLayout.setObjectName(u"stepLayout")

        self.horizontalLayout.addLayout(self.stepLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1400, 33))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_load_state)
        self.menuFile.addAction(self.action_save_state)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_info)
        self.menuFile.addAction(self.action_exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GedTidy \u2013 Prototyp", None))
        self.action_load_state.setText(QCoreApplication.translate("MainWindow", u"Arbeitsstand laden", None))
        self.action_save_state.setText(QCoreApplication.translate("MainWindow", u"Arbeitsstand speichern", None))
        self.action_save_state_as.setText(QCoreApplication.translate("MainWindow", u"Speichern unter...", None))
        self.action_info.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Beenden", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
    # retranslateUi

