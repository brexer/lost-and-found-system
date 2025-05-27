# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'surrenderItem.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)

class Ui_SurrenderItemDialog(object):
    def setupUi(self, SurrenderItemDialog):
        if not SurrenderItemDialog.objectName():
            SurrenderItemDialog.setObjectName(u"SurrenderItemDialog")
        SurrenderItemDialog.resize(602, 682)
        self.stackedWidget = QStackedWidget(SurrenderItemDialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 601, 681))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.itemPage = QWidget()
        self.itemPage.setObjectName(u"itemPage")
        self.label_2 = QLabel(self.itemPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 191, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.itemNameEdit = QLineEdit(self.itemPage)
        self.itemNameEdit.setObjectName(u"itemNameEdit")
        self.itemNameEdit.setGeometry(QRect(20, 140, 301, 41))
        self.itemNameEdit.setStyleSheet(u"QLineEdit {\n"
"        border: 2px solid #ccc;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }")
        self.label_3 = QLabel(self.itemPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 80, 23))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.locationFoundEdit = QLineEdit(self.itemPage)
        self.locationFoundEdit.setObjectName(u"locationFoundEdit")
        self.locationFoundEdit.setGeometry(QRect(320, 220, 271, 41))
        self.locationFoundEdit.setStyleSheet(u"QLineEdit {\n"
"        border: 2px solid #ccc;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }")
        self.label_5 = QLabel(self.itemPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 190, 191, 23))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.itemPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 190, 211, 23))
        self.label_6.setFont(font1)
        self.descriptionEdit = QLineEdit(self.itemPage)
        self.descriptionEdit.setObjectName(u"descriptionEdit")
        self.descriptionEdit.setGeometry(QRect(20, 300, 561, 61))
        self.descriptionEdit.setStyleSheet(u"QLineEdit {\n"
"        border: 2px solid #ccc;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }")
        self.label_7 = QLabel(self.itemPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 270, 191, 23))
        self.label_7.setFont(font1)
        self.nextButton = QPushButton(self.itemPage)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(369, 610, 211, 51))
        font2 = QFont()
        font2.setPointSize(14)
        self.nextButton.setFont(font2)
        self.nextButton.setStyleSheet(u"QPushButton {\n"
"        background-color: rgb(170, 0, 0);\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 20px;\n"
"        padding: 8px 16px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #800000;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #4d0000;\n"
"    }")
        self.cancelButton = QPushButton(self.itemPage)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(20, 610, 211, 51))
        self.cancelButton.setFont(font2)
        self.cancelButton.setStyleSheet(u"QPushButton {\n"
"        border: 1px solid;\n"
"        border-radius: 20px;\n"
"        padding: 8px 16px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightgray;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: gray;\n"
"    }")
        self.frame_2 = QFrame(self.itemPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 611, 80))
        self.frame_2.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(190, 0, 231, 81))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.dateFoundEdit = QDateTimeEdit(self.itemPage)
        self.dateFoundEdit.setObjectName(u"dateFoundEdit")
        self.dateFoundEdit.setGeometry(QRect(20, 220, 271, 41))
        self.dateFoundEdit.setFont(font1)
        self.dateFoundEdit.setCalendarPopup(True)
        self.label_14 = QLabel(self.itemPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(380, 110, 191, 23))
        self.label_14.setFont(font1)
        self.comboBox_2 = QComboBox(self.itemPage)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(370, 140, 201, 41))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.comboBox_2.setFont(font4)
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"        border: 2px solid #ccc;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }")
        self.itemImageButton = QPushButton(self.itemPage)
        self.itemImageButton.setObjectName(u"itemImageButton")
        self.itemImageButton.setGeometry(QRect(470, 470, 101, 31))
        self.itemImageButton.setStyleSheet(u"QPushButton {\n"
"        background-color: rgb(170, 0, 0);\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 20px;\n"
"        padding: 8px 16px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #800000;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #4d0000;\n"
"    }")
        self.itemImagePreview = QLabel(self.itemPage)
        self.itemImagePreview.setObjectName(u"itemImagePreview")
        self.itemImagePreview.setGeometry(QRect(30, 400, 431, 191))
        self.itemImagePreview.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.itemPage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 370, 111, 23))
        self.label_15.setFont(font1)
        self.stackedWidget.addWidget(self.itemPage)
        self.personPage = QWidget()
        self.personPage.setObjectName(u"personPage")
        self.label_8 = QLabel(self.personPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 330, 191, 23))
        self.label_8.setFont(font1)
        self.phoneNumberEdit = QLineEdit(self.personPage)
        self.phoneNumberEdit.setObjectName(u"phoneNumberEdit")
        self.phoneNumberEdit.setGeometry(QRect(21, 280, 271, 41))
        self.phoneNumberEdit.setStyleSheet(u"QLineEdit {\n"
"        border: 2px solid #ccc;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }")
        self.cancelButton_2 = QPushButton(self.personPage)
        self.cancelButton_2.setObjectName(u"cancelButton_2")
        self.cancelButton_2.setGeometry(QRect(21, 610, 211, 51))
        self.cancelButton_2.setFont(font2)
        self.cancelButton_2.setStyleSheet(u"QPushButton {\n"
"        border: 1px solid;\n"
"        border-radius: 20px;\n"
"        padding: 8px 16px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightgray;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: gray;\n"
"    }")
        self.label_9 = QLabel(self.personPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(31, 160, 80, 23))
        self.label_9.setFont(font1)
        self.label_10 = QLabel(self.personPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(31, 250, 191, 23))
        self.label_10.setFont(font1)
        self.firstNameEdit = QLineEdit(self.personPage)
        self.firstNameEdit.setObjectName(u"firstNameEdit")
        self.firstNameEdit.setGeometry(QRect(20, 190, 271, 41))
        self.firstNameEdit.setStyleSheet(u"QLineEdit {\n"
"        border: 2px solid #ccc;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }")
        self.confirmButton = QPushButton(self.personPage)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setGeometry(QRect(370, 610, 211, 51))
        self.confirmButton.setFont(font2)
        self.confirmButton.setStyleSheet(u"QPushButton {\n"
"        background-color: rgb(170, 0, 0);\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 20px;\n"
"        padding: 8px 16px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #800000;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #4d0000;\n"
"    }")
        self.label_12 = QLabel(self.personPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(320, 250, 191, 23))
        self.label_12.setFont(font1)
        self.label_13 = QLabel(self.personPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(21, 90, 251, 41))
        self.label_13.setFont(font)
        self.lastNameEdit = QLineEdit(self.personPage)
        self.lastNameEdit.setObjectName(u"lastNameEdit")
        self.lastNameEdit.setGeometry(QRect(310, 190, 271, 41))
        self.lastNameEdit.setStyleSheet(u"QLineEdit {\n"
"        border: 2px solid #ccc;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }")
        self.frame = QFrame(self.personPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 611, 80))
        self.frame.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 0, 221, 81))
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.backButton = QPushButton(self.frame)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(20, 20, 60, 31))
        self.backButton.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 1px solid;\n"
"    border-radius: 10px;\n"
"    padding: 4px 6px;\n"
"    font-size: 10pt;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"}")
        self.departmentEdit_2 = QLineEdit(self.personPage)
        self.departmentEdit_2.setObjectName(u"departmentEdit_2")
        self.departmentEdit_2.setGeometry(QRect(310, 280, 271, 41))
        self.departmentEdit_2.setStyleSheet(u"QLineEdit {\n"
"        border: 2px solid #ccc;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }")
        self.proofImagePreview = QLabel(self.personPage)
        self.proofImagePreview.setObjectName(u"proofImagePreview")
        self.proofImagePreview.setGeometry(QRect(20, 360, 441, 231))
        self.proofImagePreview.setAlignment(Qt.AlignCenter)
        self.proofImageButton = QPushButton(self.personPage)
        self.proofImageButton.setObjectName(u"proofImageButton")
        self.proofImageButton.setGeometry(QRect(470, 470, 101, 31))
        self.proofImageButton.setStyleSheet(u"QPushButton {\n"
"        background-color: rgb(170, 0, 0);\n"
"        color: white;\n"
"        border: none;\n"
"        border-radius: 20px;\n"
"        padding: 8px 16px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #800000;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #4d0000;\n"
"    }")
        self.stackedWidget.addWidget(self.personPage)

        self.retranslateUi(SurrenderItemDialog)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SurrenderItemDialog)
    # setupUi

    def retranslateUi(self, SurrenderItemDialog):
        SurrenderItemDialog.setWindowTitle(QCoreApplication.translate("SurrenderItemDialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("SurrenderItemDialog", u"Item Details", None))
        self.itemNameEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("SurrenderItemDialog", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("SurrenderItemDialog", u"Date Found", None))
        self.label_6.setText(QCoreApplication.translate("SurrenderItemDialog", u"Location Found", None))
        self.descriptionEdit.setText("")
        self.label_7.setText(QCoreApplication.translate("SurrenderItemDialog", u"Description", None))
        self.nextButton.setText(QCoreApplication.translate("SurrenderItemDialog", u"Next", None))
        self.cancelButton.setText(QCoreApplication.translate("SurrenderItemDialog", u"Cancel", None))
        self.label_11.setText(QCoreApplication.translate("SurrenderItemDialog", u"Surrender an Item", None))
        self.label_14.setText(QCoreApplication.translate("SurrenderItemDialog", u"Category", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("SurrenderItemDialog", u"Electronics", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("SurrenderItemDialog", u"School Supplies", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("SurrenderItemDialog", u"Clothing and Accessories", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("SurrenderItemDialog", u"I.D Cards", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("SurrenderItemDialog", u"Wallets ", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("SurrenderItemDialog", u"Keys", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("SurrenderItemDialog", u"Personal Items", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("SurrenderItemDialog", u"Others", None))

        self.itemImageButton.setText(QCoreApplication.translate("SurrenderItemDialog", u"Upload ", None))
        self.itemImagePreview.setText(QCoreApplication.translate("SurrenderItemDialog", u"No Image Selected", None))
        self.label_15.setText(QCoreApplication.translate("SurrenderItemDialog", u"Item Image", None))
        self.label_8.setText(QCoreApplication.translate("SurrenderItemDialog", u"Proof ID", None))
        self.phoneNumberEdit.setPlaceholderText(QCoreApplication.translate("SurrenderItemDialog", u"e.g. 09123456789", None))
        self.cancelButton_2.setText(QCoreApplication.translate("SurrenderItemDialog", u"Cancel", None))
        self.label_9.setText(QCoreApplication.translate("SurrenderItemDialog", u"Name", None))
        self.label_10.setText(QCoreApplication.translate("SurrenderItemDialog", u"Phone Number", None))
        self.firstNameEdit.setPlaceholderText(QCoreApplication.translate("SurrenderItemDialog", u"First Name", None))
        self.confirmButton.setText(QCoreApplication.translate("SurrenderItemDialog", u"Confirm", None))
        self.label_12.setText(QCoreApplication.translate("SurrenderItemDialog", u"Department", None))
        self.label_13.setText(QCoreApplication.translate("SurrenderItemDialog", u"Personal Details", None))
        self.lastNameEdit.setPlaceholderText(QCoreApplication.translate("SurrenderItemDialog", u"Last Name", None))
        self.label.setText(QCoreApplication.translate("SurrenderItemDialog", u"Surrender an Item", None))
        self.backButton.setText(QCoreApplication.translate("SurrenderItemDialog", u"Back", None))
        self.departmentEdit_2.setPlaceholderText(QCoreApplication.translate("SurrenderItemDialog", u"e.g. BSCS", None))
        self.proofImagePreview.setText(QCoreApplication.translate("SurrenderItemDialog", u"No Image Selected", None))
        self.proofImageButton.setText(QCoreApplication.translate("SurrenderItemDialog", u"Upload", None))
    # retranslateUi

