# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1127, 691)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.sidebar)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(14)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.label_3 = QLabel(self.sidebar)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setMargin(5)
        self.label_3.setIndent(-1)

        self.verticalLayout_3.addWidget(self.label_3)

        self.homeButton = QPushButton(self.sidebar)
        self.homeButton.setObjectName(u"homeButton")
        font1 = QFont()
        self.homeButton.setFont(font1)
        self.homeButton.setIconSize(QSize(20, 20))
        self.homeButton.setCheckable(True)
        self.homeButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.homeButton)

        self.lostButton = QPushButton(self.sidebar)
        self.lostButton.setObjectName(u"lostButton")
        self.lostButton.setFont(font1)
        self.lostButton.setIconSize(QSize(20, 20))
        self.lostButton.setCheckable(True)
        self.lostButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.lostButton)

        self.foundButton = QPushButton(self.sidebar)
        self.foundButton.setObjectName(u"foundButton")
        self.foundButton.setFont(font1)
        self.foundButton.setIconSize(QSize(20, 20))
        self.foundButton.setCheckable(True)
        self.foundButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.foundButton)

        self.claimedButton = QPushButton(self.sidebar)
        self.claimedButton.setObjectName(u"claimedButton")
        self.claimedButton.setFont(font1)
        self.claimedButton.setIconSize(QSize(20, 20))
        self.claimedButton.setCheckable(True)
        self.claimedButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.claimedButton)

        self.reportButton = QPushButton(self.sidebar)
        self.reportButton.setObjectName(u"reportButton")
        self.reportButton.setFont(font1)
        self.reportButton.setIconSize(QSize(20, 20))
        self.reportButton.setCheckable(True)
        self.reportButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.reportButton)

        self.verticalSpacer_2 = QSpacerItem(20, 528, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(14)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settingsButton = QPushButton(self.sidebar)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setFont(font1)
        self.settingsButton.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.settingsButton)

        self.logoutButton = QPushButton(self.sidebar)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setFont(font1)
        self.logoutButton.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.logoutButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout.addWidget(self.sidebar)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(8)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topbar = QWidget(self.widget_2)
        self.topbar.setObjectName(u"topbar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.topbar.sizePolicy().hasHeightForWidth())
        self.topbar.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.topbar)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(14)
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.label_25 = QLabel(self.homePage)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(0, 40, 581, 51))
        self.label_25.setStyleSheet(u"QLabel {\n"
"    padding: 8px 12px;\n"
"    color: #1E1E1E;\n"
"    font: 20pt \"Futura\";\n"
"    font-weight: bold; \n"
"}")
        self.label_4 = QLabel(self.homePage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 80, 531, 41))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    padding: 8px 12px;\n"
"    color: #1E1E1E;\n"
"    font: 10pt \"Century Gothic\";\n"
"	weight: bold;\n"
"}")
        self.outisideFrame = QFrame(self.homePage)
        self.outisideFrame.setObjectName(u"outisideFrame")
        self.outisideFrame.setGeometry(QRect(10, 120, 921, 371))
        self.outisideFrame.setStyleSheet(u"")
        self.outisideFrame.setFrameShape(QFrame.StyledPanel)
        self.outisideFrame.setFrameShadow(QFrame.Raised)
        self.label_26 = QLabel(self.outisideFrame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 10, 151, 41))
        self.label_26.setStyleSheet(u"QLabel {\n"
"    padding: 8px 12px;\n"
"    color: #1E1E1E;\n"
"    font: 13pt \"Futura\";\n"
"	font-weight: bold; \n"
"}")
        self.layoutWidget = QWidget(self.outisideFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 50, 821, 301))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 161, 181))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_27 = QLabel(self.frame_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 200, 121, 91))

        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.layoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 10, 161, 181))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 200, 121, 91))

        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.layoutWidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 10, 161, 181))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_29 = QLabel(self.frame_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 200, 121, 91))

        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.layoutWidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 10, 161, 181))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 200, 121, 91))

        self.horizontalLayout_5.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.homePage)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 490, 921, 221))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.homePage)
        self.ReportedItems = QWidget()
        self.ReportedItems.setObjectName(u"ReportedItems")
        self.verticalLayout_7 = QVBoxLayout(self.ReportedItems)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget = QTableWidget(self.ReportedItems)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_7.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.ReportedItems)
        self.SurrenderedItems = QWidget()
        self.SurrenderedItems.setObjectName(u"SurrenderedItems")
        self.label_10 = QLabel(self.SurrenderedItems)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(490, 220, 151, 16))
        self.stackedWidget.addWidget(self.SurrenderedItems)
        self.ClaimedItems = QWidget()
        self.ClaimedItems.setObjectName(u"ClaimedItems")
        self.label_7 = QLabel(self.ClaimedItems)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 390, 81, 16))
        self.stackedWidget.addWidget(self.ClaimedItems)
        self.myreportPage = QWidget()
        self.myreportPage.setObjectName(u"myreportPage")
        self.label_8 = QLabel(self.myreportPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(390, 380, 131, 16))
        self.stackedWidget.addWidget(self.myreportPage)
        self.ManagePersons = QWidget()
        self.ManagePersons.setObjectName(u"ManagePersons")
        self.label_9 = QLabel(self.ManagePersons)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(440, 400, 211, 61))
        self.stackedWidget.addWidget(self.ManagePersons)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lost and Found", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.lostButton.setText(QCoreApplication.translate("MainWindow", u"Lost Items", None))
        self.foundButton.setText(QCoreApplication.translate("MainWindow", u"Found Items", None))
        self.claimedButton.setText(QCoreApplication.translate("MainWindow", u"Claimed Items", None))
        self.reportButton.setText(QCoreApplication.translate("MainWindow", u"Report Item", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Manage Persons", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Lost and Found System!", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Let us help you find what you're looking for or return something you found.", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Recent Items", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"SurrenderedItems", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Claimed Items", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Report Item", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Manage Persons (accessible by admin)", None))
    # retranslateUi

