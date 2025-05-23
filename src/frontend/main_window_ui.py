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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1163, 805)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
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
        self.LostandFound = QLabel(self.sidebar)
        self.LostandFound.setObjectName(u"LostandFound")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LostandFound.sizePolicy().hasHeightForWidth())
        self.LostandFound.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.LostandFound.setFont(font)
        self.LostandFound.setMargin(5)
        self.LostandFound.setIndent(-1)

        self.verticalLayout_3.addWidget(self.LostandFound)

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
        self.manageButton = QPushButton(self.sidebar)
        self.manageButton.setObjectName(u"manageButton")
        self.manageButton.setFont(font1)
        self.manageButton.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.manageButton)

        self.exitButton = QPushButton(self.sidebar)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setFont(font1)
        self.exitButton.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.exitButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout.addWidget(self.sidebar)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(8)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.outisideFrame = QFrame(self.homePage)
        self.outisideFrame.setObjectName(u"outisideFrame")
        self.outisideFrame.setGeometry(QRect(0, 120, 921, 381))
        self.outisideFrame.setStyleSheet(u"")
        self.outisideFrame.setFrameShape(QFrame.StyledPanel)
        self.outisideFrame.setFrameShadow(QFrame.Raised)
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

        self.layoutWidget1 = QWidget(self.homePage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 80, 921, 39))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.layoutWidget1)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"QLabel {\n"
"    padding: 8px 12px;\n"
"    color: #1E1E1E;\n"
"    font: 13pt \"Futura\";\n"
"	font-weight: bold; \n"
"}")

        self.horizontalLayout_2.addWidget(self.label_26)

        self.horizontalSpacer = QSpacerItem(698, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.layoutWidget2 = QWidget(self.homePage)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 587, 90))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.layoutWidget2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"QLabel {\n"
"    padding: 8px 12px;\n"
"    color: #1E1E1E;\n"
"    font: 20pt \"Futura\";\n"
"    font-weight: bold; \n"
"}")

        self.verticalLayout_8.addWidget(self.label_25)

        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    padding: 8px 12px;\n"
"    color: #1E1E1E;\n"
"    font: 10pt \"Century Gothic\";\n"
"	weight: bold;\n"
"}")

        self.verticalLayout_8.addWidget(self.label_4)

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
        self.stackedWidget.addWidget(self.SurrenderedItems)
        self.ClaimedItems = QWidget()
        self.ClaimedItems.setObjectName(u"ClaimedItems")
        self.label_7 = QLabel(self.ClaimedItems)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 390, 81, 16))
        self.stackedWidget.addWidget(self.ClaimedItems)
        self.myreportPage = QWidget()
        self.myreportPage.setObjectName(u"myreportPage")
        self.layoutWidget_2 = QWidget(self.myreportPage)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(80, 210, 122, 60))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_13 = QLabel(self.layoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.horizontalSpacer_4 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.lineEdit_4 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")

        self.verticalLayout_10.addWidget(self.lineEdit_4)

        self.layoutWidget_3 = QWidget(self.myreportPage)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(80, 280, 96, 50))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(self.layoutWidget_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_9)

        self.dateEdit = QDateEdit(self.layoutWidget_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.dateEdit)

        self.label_6 = QLabel(self.myreportPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 0, 211, 16))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.lineEdit_13 = QLineEdit(self.myreportPage)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(90, 620, 251, 31))
        self.lineEdit_13.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.label_19 = QLabel(self.myreportPage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(90, 520, 101, 16))
        self.layoutWidget_4 = QWidget(self.myreportPage)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(340, 210, 134, 61))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.layoutWidget_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_7.addWidget(self.label_14)

        self.horizontalSpacer_5 = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.lineEdit_6 = QLineEdit(self.layoutWidget_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")

        self.verticalLayout_11.addWidget(self.lineEdit_6)

        self.layoutWidget_5 = QWidget(self.myreportPage)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(80, 350, 561, 60))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_17 = QLabel(self.layoutWidget_5)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_10.addWidget(self.label_17)

        self.horizontalSpacer_8 = QSpacerItem(498, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_14.addLayout(self.horizontalLayout_10)

        self.lineEdit_7 = QLineEdit(self.layoutWidget_5)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")

        self.verticalLayout_14.addWidget(self.lineEdit_7)

        self.layoutWidget_6 = QWidget(self.myreportPage)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(90, 410, 549, 22))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.label_18 = QLabel(self.layoutWidget_6)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.layoutWidget_7 = QWidget(self.myreportPage)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(90, 550, 243, 57))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_20 = QLabel(self.layoutWidget_7)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_12.addWidget(self.label_20)

        self.horizontalSpacer_12 = QSpacerItem(178, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.verticalLayout_15.addLayout(self.horizontalLayout_12)

        self.lineEdit_9 = QLineEdit(self.layoutWidget_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")

        self.verticalLayout_15.addWidget(self.lineEdit_9)

        self.lineEdit_14 = QLineEdit(self.myreportPage)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(360, 620, 251, 31))
        self.lineEdit_14.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.frame = QFrame(self.myreportPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 430, 571, 80))
        self.frame.setStyleSheet(u"QFrame {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.pushButton_21 = QPushButton(self.frame)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(250, 10, 50, 30))
        self.pushButton_21.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow-down-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_21.setIcon(icon)
        self.pushButton_21.setIconSize(QSize(20, 20))
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setAutoExclusive(True)
        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(210, 50, 151, 16))
        self.layoutWidget_8 = QWidget(self.myreportPage)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(80, 80, 571, 124))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.layoutWidget_8)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.horizontalSpacer_2 = QSpacerItem(498, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.lineEdit_2 = QLineEdit(self.layoutWidget_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")

        self.verticalLayout_9.addWidget(self.lineEdit_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_12 = QLabel(self.layoutWidget_8)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.horizontalSpacer_3 = QSpacerItem(428, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.lineEdit_3 = QLineEdit(self.layoutWidget_8)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")

        self.verticalLayout_9.addWidget(self.lineEdit_3)

        self.layoutWidget_9 = QWidget(self.myreportPage)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(370, 550, 182, 60))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_21 = QLabel(self.layoutWidget_9)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_13.addWidget(self.label_21)

        self.horizontalSpacer_13 = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)


        self.verticalLayout_16.addLayout(self.horizontalLayout_13)

        self.lineEdit_10 = QLineEdit(self.layoutWidget_9)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")

        self.verticalLayout_16.addWidget(self.lineEdit_10)

        self.pushButton_22 = QPushButton(self.myreportPage)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(250, 660, 203, 30))
        self.pushButton_22.setFont(font1)
        self.pushButton_22.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_22.setIcon(icon1)
        self.pushButton_22.setIconSize(QSize(20, 20))
        self.layoutWidget_10 = QWidget(self.myreportPage)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(340, 278, 134, 61))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_24 = QLabel(self.layoutWidget_10)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_15.addWidget(self.label_24)

        self.horizontalSpacer_16 = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)


        self.verticalLayout_17.addLayout(self.horizontalLayout_15)

        self.lineEdit_11 = QLineEdit(self.layoutWidget_10)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")

        self.verticalLayout_17.addWidget(self.lineEdit_11)

        self.lostButton_2 = QRadioButton(self.myreportPage)
        self.lostButton_2.setObjectName(u"lostButton_2")
        self.lostButton_2.setGeometry(QRect(240, 50, 82, 17))
        self.foundButton_2 = QRadioButton(self.myreportPage)
        self.foundButton_2.setObjectName(u"foundButton_2")
        self.foundButton_2.setGeometry(QRect(450, 50, 82, 17))
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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LostandFound.setText(QCoreApplication.translate("MainWindow", u"Lost and Found", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.lostButton.setText(QCoreApplication.translate("MainWindow", u"Lost Items", None))
        self.foundButton.setText(QCoreApplication.translate("MainWindow", u"Found Items", None))
        self.claimedButton.setText(QCoreApplication.translate("MainWindow", u"Claimed Items", None))
        self.reportButton.setText(QCoreApplication.translate("MainWindow", u"Report Item", None))
        self.manageButton.setText(QCoreApplication.translate("MainWindow", u"Manage Persons", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Recent Items", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Lost and Found System!", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Let us help you find what you're looking for or return something you found.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Claimed Items", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Date Lost", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Lost and Found Report Form", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Contact Information:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Size (if applicable)", None))
        self.lineEdit_6.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Photos", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.lineEdit_14.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.pushButton_21.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Drag Photos here, or Browse", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Item Details", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Brand/Model (if applicable)", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.lineEdit_11.setText("")
        self.lostButton_2.setText(QCoreApplication.translate("MainWindow", u"Lost", None))
        self.foundButton_2.setText(QCoreApplication.translate("MainWindow", u"Found", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Manage Persons (accessible by admin)", None))
    # retranslateUi

