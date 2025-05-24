# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1313, 953)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(200, 0, 1111, 961))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.layoutWidget_6 = QWidget(self.homePage)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(0, 0, 587, 90))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.layoutWidget_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"QLabel {\n"
"    padding: 8px 12px;\n"
"    color: #1E1E1E;\n"
"    font: 20pt \"Futura\";\n"
"    font-weight: bold; \n"
"}")

        self.verticalLayout_8.addWidget(self.label_25)

        self.label_8 = QLabel(self.layoutWidget_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"    padding: 8px 12px;\n"
"    color: #1E1E1E;\n"
"    font: 10pt \"Century Gothic\";\n"
"	weight: bold;\n"
"}")

        self.verticalLayout_8.addWidget(self.label_8)

        self.layoutWidget_7 = QWidget(self.homePage)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(0, 90, 921, 39))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.layoutWidget_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"QLabel {\n"
"    padding: 8px 12px;\n"
"    color: #1E1E1E;\n"
"    font: 13pt \"Futura\";\n"
"	font-weight: bold; \n"
"}")

        self.horizontalLayout_6.addWidget(self.label_26)

        self.horizontalSpacer = QSpacerItem(698, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.layoutWidget_8 = QWidget(self.homePage)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(30, 140, 981, 291))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.recentFrame1_2 = QFrame(self.layoutWidget_8)
        self.recentFrame1_2.setObjectName(u"recentFrame1_2")
        self.recentFrame1_2.setFrameShape(QFrame.StyledPanel)
        self.recentFrame1_2.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.recentFrame1_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 10, 171, 181))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_36 = QLabel(self.recentFrame1_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, 200, 121, 21))

        self.horizontalLayout_8.addWidget(self.recentFrame1_2)

        self.recentFrame2_2 = QFrame(self.layoutWidget_8)
        self.recentFrame2_2.setObjectName(u"recentFrame2_2")
        self.recentFrame2_2.setFrameShape(QFrame.StyledPanel)
        self.recentFrame2_2.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.recentFrame2_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(10, 10, 171, 181))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_37 = QLabel(self.recentFrame2_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 200, 121, 21))

        self.horizontalLayout_8.addWidget(self.recentFrame2_2)

        self.recentFrame3_2 = QFrame(self.layoutWidget_8)
        self.recentFrame3_2.setObjectName(u"recentFrame3_2")
        self.recentFrame3_2.setFrameShape(QFrame.StyledPanel)
        self.recentFrame3_2.setFrameShadow(QFrame.Raised)
        self.frame_16 = QFrame(self.recentFrame3_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(10, 10, 171, 181))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.label_38 = QLabel(self.recentFrame3_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 200, 121, 21))

        self.horizontalLayout_8.addWidget(self.recentFrame3_2)

        self.recentFrame4_2 = QFrame(self.layoutWidget_8)
        self.recentFrame4_2.setObjectName(u"recentFrame4_2")
        self.recentFrame4_2.setFrameShape(QFrame.StyledPanel)
        self.recentFrame4_2.setFrameShadow(QFrame.Raised)
        self.frame_18 = QFrame(self.recentFrame4_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(10, 10, 171, 181))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_39 = QLabel(self.recentFrame4_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 200, 121, 21))

        self.horizontalLayout_8.addWidget(self.recentFrame4_2)

        self.recentFram5_2 = QFrame(self.layoutWidget_8)
        self.recentFram5_2.setObjectName(u"recentFram5_2")
        self.recentFram5_2.setFrameShape(QFrame.StyledPanel)
        self.recentFram5_2.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.recentFram5_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(10, 10, 171, 181))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_40 = QLabel(self.recentFram5_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 200, 121, 21))

        self.horizontalLayout_8.addWidget(self.recentFram5_2)

        self.stackedWidget.addWidget(self.homePage)
        self.managePersonsPage = QWidget()
        self.managePersonsPage.setObjectName(u"managePersonsPage")
        self.label_3 = QLabel(self.managePersonsPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 681, 101))
        font = QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.personTable = QTableWidget(self.managePersonsPage)
        if (self.personTable.columnCount() < 6):
            self.personTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.personTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.personTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.personTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.personTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.personTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.personTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.personTable.setObjectName(u"personTable")
        self.personTable.setGeometry(QRect(10, 180, 1091, 671))
        self.pushButton_7 = QPushButton(self.managePersonsPage)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(990, 860, 112, 34))
        self.pushButton_8 = QPushButton(self.managePersonsPage)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 860, 112, 34))
        self.personSearchEdit = QLineEdit(self.managePersonsPage)
        self.personSearchEdit.setObjectName(u"personSearchEdit")
        self.personSearchEdit.setGeometry(QRect(10, 130, 401, 41))
        self.personSearchEdit.setStyleSheet(u"QLineEdit {\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 15px;\n"
"                padding: 6px 12px;\n"
"                background-color: #f9f9f9;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #0078d7;\n"
"                background-color: #ffffff;\n"
"            }")
        self.personSearchButton = QPushButton(self.managePersonsPage)
        self.personSearchButton.setObjectName(u"personSearchButton")
        self.personSearchButton.setGeometry(QRect(430, 130, 112, 41))
        self.personSearchButton.setStyleSheet(u"QPushButton {\n"
"                background-color: maroon;\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 20px;\n"
"                padding: 8px 16px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #a00000;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #700000;\n"
"            }")
        self.layoutWidget = QWidget(self.managePersonsPage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(390, 850, 341, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.personPrev = QPushButton(self.layoutWidget)
        self.personPrev.setObjectName(u"personPrev")

        self.horizontalLayout.addWidget(self.personPrev)

        self.personPageLabel = QLabel(self.layoutWidget)
        self.personPageLabel.setObjectName(u"personPageLabel")

        self.horizontalLayout.addWidget(self.personPageLabel)

        self.personNext = QPushButton(self.layoutWidget)
        self.personNext.setObjectName(u"personNext")

        self.horizontalLayout.addWidget(self.personNext)

        self.stackedWidget.addWidget(self.managePersonsPage)
        self.manageItemsPage = QWidget()
        self.manageItemsPage.setObjectName(u"manageItemsPage")
        self.label_7 = QLabel(self.manageItemsPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 10, 401, 111))
        self.label_7.setFont(font)
        self.itemUpdateButton = QPushButton(self.manageItemsPage)
        self.itemUpdateButton.setObjectName(u"itemUpdateButton")
        self.itemUpdateButton.setGeometry(QRect(990, 850, 112, 34))
        self.itemTable = QTableWidget(self.manageItemsPage)
        if (self.itemTable.columnCount() < 5):
            self.itemTable.setColumnCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.itemTable.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        self.itemTable.setObjectName(u"itemTable")
        self.itemTable.setGeometry(QRect(10, 180, 1091, 661))
        self.itemDeleteButton = QPushButton(self.manageItemsPage)
        self.itemDeleteButton.setObjectName(u"itemDeleteButton")
        self.itemDeleteButton.setGeometry(QRect(10, 850, 112, 34))
        self.itemSearchButton = QPushButton(self.manageItemsPage)
        self.itemSearchButton.setObjectName(u"itemSearchButton")
        self.itemSearchButton.setGeometry(QRect(430, 130, 112, 41))
        self.itemSearchButton.setStyleSheet(u"QPushButton {\n"
"                background-color: maroon;\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 20px;\n"
"                padding: 8px 16px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #a00000;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #700000;\n"
"            }")
        self.itemSearchEdit = QLineEdit(self.manageItemsPage)
        self.itemSearchEdit.setObjectName(u"itemSearchEdit")
        self.itemSearchEdit.setGeometry(QRect(10, 130, 401, 41))
        self.itemSearchEdit.setStyleSheet(u"QLineEdit {\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 15px;\n"
"                padding: 6px 12px;\n"
"                background-color: #f9f9f9;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #0078d7;\n"
"                background-color: #ffffff;\n"
"            }")
        self.layoutWidget_5 = QWidget(self.manageItemsPage)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(390, 850, 341, 51))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.itemPrevButton = QPushButton(self.layoutWidget_5)
        self.itemPrevButton.setObjectName(u"itemPrevButton")

        self.horizontalLayout_5.addWidget(self.itemPrevButton)

        self.personPageLabel_2 = QLabel(self.layoutWidget_5)
        self.personPageLabel_2.setObjectName(u"personPageLabel_2")

        self.horizontalLayout_5.addWidget(self.personPageLabel_2)

        self.itemNextButton = QPushButton(self.layoutWidget_5)
        self.itemNextButton.setObjectName(u"itemNextButton")

        self.horizontalLayout_5.addWidget(self.itemNextButton)

        self.stackedWidget.addWidget(self.manageItemsPage)
        self.reportedItems = QWidget()
        self.reportedItems.setObjectName(u"reportedItems")
        self.claimSearchEdit = QLineEdit(self.reportedItems)
        self.claimSearchEdit.setObjectName(u"claimSearchEdit")
        self.claimSearchEdit.setGeometry(QRect(10, 130, 401, 41))
        self.claimSearchEdit.setStyleSheet(u"QLineEdit {\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 15px;\n"
"                padding: 6px 12px;\n"
"                background-color: #f9f9f9;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #0078d7;\n"
"                background-color: #ffffff;\n"
"            }")
        self.claimTable = QTableWidget(self.reportedItems)
        if (self.claimTable.columnCount() < 5):
            self.claimTable.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.claimTable.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.claimTable.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.claimTable.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.claimTable.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.claimTable.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.claimTable.setObjectName(u"claimTable")
        self.claimTable.setGeometry(QRect(10, 180, 1091, 661))
        self.deleteClaimButton = QPushButton(self.reportedItems)
        self.deleteClaimButton.setObjectName(u"deleteClaimButton")
        self.deleteClaimButton.setGeometry(QRect(10, 860, 112, 34))
        self.claimSearchButton = QPushButton(self.reportedItems)
        self.claimSearchButton.setObjectName(u"claimSearchButton")
        self.claimSearchButton.setGeometry(QRect(430, 130, 112, 41))
        self.claimSearchButton.setStyleSheet(u"QPushButton {\n"
"                background-color: maroon;\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 20px;\n"
"                padding: 8px 16px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #a00000;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #700000;\n"
"            }")
        self.layoutWidget_2 = QWidget(self.reportedItems)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(390, 850, 341, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.claimPrev = QPushButton(self.layoutWidget_2)
        self.claimPrev.setObjectName(u"claimPrev")

        self.horizontalLayout_2.addWidget(self.claimPrev)

        self.claimPageLabel = QLabel(self.layoutWidget_2)
        self.claimPageLabel.setObjectName(u"claimPageLabel")

        self.horizontalLayout_2.addWidget(self.claimPageLabel)

        self.claimNext = QPushButton(self.layoutWidget_2)
        self.claimNext.setObjectName(u"claimNext")

        self.horizontalLayout_2.addWidget(self.claimNext)

        self.updateClaimButton = QPushButton(self.reportedItems)
        self.updateClaimButton.setObjectName(u"updateClaimButton")
        self.updateClaimButton.setGeometry(QRect(990, 860, 112, 34))
        self.label_9 = QLabel(self.reportedItems)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 401, 111))
        self.label_9.setFont(font)
        self.stackedWidget.addWidget(self.reportedItems)
        self.claimedItems = QWidget()
        self.claimedItems.setObjectName(u"claimedItems")
        self.reportSearchEdit = QLineEdit(self.claimedItems)
        self.reportSearchEdit.setObjectName(u"reportSearchEdit")
        self.reportSearchEdit.setGeometry(QRect(10, 130, 401, 41))
        self.reportSearchEdit.setStyleSheet(u"QLineEdit {\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 15px;\n"
"                padding: 6px 12px;\n"
"                background-color: #f9f9f9;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #0078d7;\n"
"                background-color: #ffffff;\n"
"            }")
        self.layoutWidget_3 = QWidget(self.claimedItems)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(390, 850, 341, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.reportPrev = QPushButton(self.layoutWidget_3)
        self.reportPrev.setObjectName(u"reportPrev")

        self.horizontalLayout_3.addWidget(self.reportPrev)

        self.reportPageLabel = QLabel(self.layoutWidget_3)
        self.reportPageLabel.setObjectName(u"reportPageLabel")

        self.horizontalLayout_3.addWidget(self.reportPageLabel)

        self.reportNext = QPushButton(self.layoutWidget_3)
        self.reportNext.setObjectName(u"reportNext")

        self.horizontalLayout_3.addWidget(self.reportNext)

        self.reportUpdateButton = QPushButton(self.claimedItems)
        self.reportUpdateButton.setObjectName(u"reportUpdateButton")
        self.reportUpdateButton.setGeometry(QRect(990, 860, 112, 34))
        self.deleteClaimButton_2 = QPushButton(self.claimedItems)
        self.deleteClaimButton_2.setObjectName(u"deleteClaimButton_2")
        self.deleteClaimButton_2.setGeometry(QRect(10, 860, 112, 34))
        self.reportSearchButton = QPushButton(self.claimedItems)
        self.reportSearchButton.setObjectName(u"reportSearchButton")
        self.reportSearchButton.setGeometry(QRect(430, 130, 112, 41))
        self.reportSearchButton.setStyleSheet(u"QPushButton {\n"
"                background-color: maroon;\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 20px;\n"
"                padding: 8px 16px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #a00000;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #700000;\n"
"            }")
        self.reportTable = QTableWidget(self.claimedItems)
        if (self.reportTable.columnCount() < 4):
            self.reportTable.setColumnCount(4)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.reportTable.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.reportTable.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.reportTable.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.reportTable.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        self.reportTable.setObjectName(u"reportTable")
        self.reportTable.setGeometry(QRect(10, 180, 1091, 661))
        self.label_10 = QLabel(self.claimedItems)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 10, 401, 111))
        self.label_10.setFont(font)
        self.stackedWidget.addWidget(self.claimedItems)
        self.surrenderedItems = QWidget()
        self.surrenderedItems.setObjectName(u"surrenderedItems")
        self.surrenderUpdateButton = QPushButton(self.surrenderedItems)
        self.surrenderUpdateButton.setObjectName(u"surrenderUpdateButton")
        self.surrenderUpdateButton.setGeometry(QRect(990, 860, 112, 34))
        self.surrenderSearchButton = QPushButton(self.surrenderedItems)
        self.surrenderSearchButton.setObjectName(u"surrenderSearchButton")
        self.surrenderSearchButton.setGeometry(QRect(430, 130, 112, 41))
        self.surrenderSearchButton.setStyleSheet(u"QPushButton {\n"
"                background-color: maroon;\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 20px;\n"
"                padding: 8px 16px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #a00000;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #700000;\n"
"            }")
        self.surrenederSearchEdit = QLineEdit(self.surrenderedItems)
        self.surrenederSearchEdit.setObjectName(u"surrenederSearchEdit")
        self.surrenederSearchEdit.setGeometry(QRect(10, 130, 401, 41))
        self.surrenederSearchEdit.setStyleSheet(u"QLineEdit {\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 15px;\n"
"                padding: 6px 12px;\n"
"                background-color: #f9f9f9;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #0078d7;\n"
"                background-color: #ffffff;\n"
"            }")
        self.layoutWidget_4 = QWidget(self.surrenderedItems)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(390, 850, 341, 51))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.surrenderPrev = QPushButton(self.layoutWidget_4)
        self.surrenderPrev.setObjectName(u"surrenderPrev")

        self.horizontalLayout_4.addWidget(self.surrenderPrev)

        self.surrenederPageLabel = QLabel(self.layoutWidget_4)
        self.surrenederPageLabel.setObjectName(u"surrenederPageLabel")

        self.horizontalLayout_4.addWidget(self.surrenederPageLabel)

        self.surrenderNext = QPushButton(self.layoutWidget_4)
        self.surrenderNext.setObjectName(u"surrenderNext")

        self.horizontalLayout_4.addWidget(self.surrenderNext)

        self.surrenderTable = QTableWidget(self.surrenderedItems)
        if (self.surrenderTable.columnCount() < 5):
            self.surrenderTable.setColumnCount(5)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.surrenderTable.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.surrenderTable.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.surrenderTable.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.surrenderTable.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.surrenderTable.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        self.surrenderTable.setObjectName(u"surrenderTable")
        self.surrenderTable.setGeometry(QRect(10, 180, 1091, 661))
        self.surrenderDeleteButton = QPushButton(self.surrenderedItems)
        self.surrenderDeleteButton.setObjectName(u"surrenderDeleteButton")
        self.surrenderDeleteButton.setGeometry(QRect(10, 860, 112, 34))
        self.label_6 = QLabel(self.surrenderedItems)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 20, 421, 91))
        self.label_6.setFont(font)
        self.stackedWidget.addWidget(self.surrenderedItems)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(0, 0, 201, 961))
        self.sidebar.setStyleSheet(u"background-color: maroon;")
        self.verticalLayout_4 = QVBoxLayout(self.sidebar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 30, 10, 0)
        self.label = QLabel(self.sidebar)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 30, -1, -1)
        self.homeButton = QPushButton(self.sidebar)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.homeButton)

        self.managePersonsButton = QPushButton(self.sidebar)
        self.managePersonsButton.setObjectName(u"managePersonsButton")
        self.managePersonsButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.managePersonsButton)

        self.manageItemsButton = QPushButton(self.sidebar)
        self.manageItemsButton.setObjectName(u"manageItemsButton")
        self.manageItemsButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.manageItemsButton)

        self.reportItem = QPushButton(self.sidebar)
        self.reportItem.setObjectName(u"reportItem")
        self.reportItem.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.reportItem.setCheckable(True)

        self.verticalLayout_3.addWidget(self.reportItem)

        self.manage_items = QFrame(self.sidebar)
        self.manage_items.setObjectName(u"manage_items")
        self.manage_items.setFrameShape(QFrame.StyledPanel)
        self.manage_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.manage_items)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.itemHistoryButton = QPushButton(self.manage_items)
        self.itemHistoryButton.setObjectName(u"itemHistoryButton")
        self.itemHistoryButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.itemHistoryButton.setCheckable(True)

        self.verticalLayout_2.addWidget(self.itemHistoryButton)

        self.item_dropdown = QFrame(self.manage_items)
        self.item_dropdown.setObjectName(u"item_dropdown")
        self.item_dropdown.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.item_dropdown.setFrameShape(QFrame.StyledPanel)
        self.item_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.item_dropdown)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.claimItemButton = QPushButton(self.item_dropdown)
        self.claimItemButton.setObjectName(u"claimItemButton")
        self.claimItemButton.setStyleSheet(u"QPushButton {\n"
"	padding-left: 5px;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: yellow; \n"
"}")
        self.claimItemButton.setCheckable(True)

        self.verticalLayout.addWidget(self.claimItemButton)

        self.reportItemButton = QPushButton(self.item_dropdown)
        self.reportItemButton.setObjectName(u"reportItemButton")
        self.reportItemButton.setStyleSheet(u"QPushButton {\n"
"	padding-left: 20px;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: yellow; \n"
"}")
        self.reportItemButton.setCheckable(True)

        self.verticalLayout.addWidget(self.reportItemButton)

        self.surrenderItemButton = QPushButton(self.item_dropdown)
        self.surrenderItemButton.setObjectName(u"surrenderItemButton")
        self.surrenderItemButton.setStyleSheet(u"QPushButton {\n"
"	padding-left: 45px;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: yellow; \n"
"}")
        self.surrenderItemButton.setCheckable(True)

        self.verticalLayout.addWidget(self.surrenderItemButton)


        self.verticalLayout_2.addWidget(self.item_dropdown)


        self.verticalLayout_3.addWidget(self.manage_items)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 614, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.itemHistoryButton.toggled.connect(self.item_dropdown.setHidden)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Lost and Found System!", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Let us help you find what you're looking for or return something you found.", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Recent Items", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Person Management Page", None))
        ___qtablewidgetitem = self.personTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"PersonID", None));
        ___qtablewidgetitem1 = self.personTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.personTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem3 = self.personTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem4 = self.personTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Department", None));
        ___qtablewidgetitem5 = self.personTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ProofID", None));
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.personSearchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.personPrev.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.personPageLabel.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.personNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Manage Items Page", None))
        self.itemUpdateButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        ___qtablewidgetitem6 = self.itemTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ItemID", None));
        ___qtablewidgetitem7 = self.itemTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem8 = self.itemTable.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem9 = self.itemTable.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem10 = self.itemTable.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.itemDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.itemSearchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.itemPrevButton.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.personPageLabel_2.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.itemNextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        ___qtablewidgetitem11 = self.claimTable.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ItemID", None));
        ___qtablewidgetitem12 = self.claimTable.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem13 = self.claimTable.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Date Lost", None));
        ___qtablewidgetitem14 = self.claimTable.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Location Lost", None));
        ___qtablewidgetitem15 = self.claimTable.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Reported By", None));
        self.deleteClaimButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.claimSearchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.claimPrev.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.claimPageLabel.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.claimNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.updateClaimButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Reported Items Page", None))
        self.reportPrev.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.reportPageLabel.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.reportNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.reportUpdateButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.deleteClaimButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.reportSearchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem16 = self.reportTable.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"ItemID", None));
        ___qtablewidgetitem17 = self.reportTable.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem18 = self.reportTable.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Date Claimed", None));
        ___qtablewidgetitem19 = self.reportTable.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Claimed By", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Claimed Items Page", None))
        self.surrenderUpdateButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.surrenderSearchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.surrenderPrev.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.surrenederPageLabel.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.surrenderNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        ___qtablewidgetitem20 = self.surrenderTable.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"ItemID", None));
        ___qtablewidgetitem21 = self.surrenderTable.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem22 = self.surrenderTable.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Date Found", None));
        ___qtablewidgetitem23 = self.surrenderTable.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Location Found", None));
        ___qtablewidgetitem24 = self.surrenderTable.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Reported By", None));
        self.surrenderDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Surrendered Items Page", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"     Lost and Found", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.managePersonsButton.setText(QCoreApplication.translate("MainWindow", u"MANAGE PERSONS", None))
        self.manageItemsButton.setText(QCoreApplication.translate("MainWindow", u"MANAGE ITEMS", None))
        self.reportItem.setText(QCoreApplication.translate("MainWindow", u"Report Item", None))
        self.itemHistoryButton.setText(QCoreApplication.translate("MainWindow", u"ITEM HISTORY", None))
        self.claimItemButton.setText(QCoreApplication.translate("MainWindow", u"Claimed", None))
        self.reportItemButton.setText(QCoreApplication.translate("MainWindow", u"Reported", None))
        self.surrenderItemButton.setText(QCoreApplication.translate("MainWindow", u"Surrendered", None))
    # retranslateUi

