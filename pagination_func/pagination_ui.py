# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagination.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1124, 977)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(100, 90, 921, 671))
        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(640, 800, 112, 34))
        self.prevButton = QPushButton(self.centralwidget)
        self.prevButton.setObjectName(u"prevButton")
        self.prevButton.setGeometry(QRect(370, 800, 112, 34))
        self.pageLabel = QLabel(self.centralwidget)
        self.pageLabel.setObjectName(u"pageLabel")
        self.pageLabel.setGeometry(QRect(520, 810, 80, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.prevButton.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.pageLabel.setText(QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi

