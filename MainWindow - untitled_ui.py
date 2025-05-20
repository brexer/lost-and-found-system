# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1153, 813)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.iconOnly = QWidget(self.centralwidget)
        self.iconOnly.setObjectName(u"iconOnly")
        self.iconOnly.setStyleSheet(u"background-color: rgb(247, 216, 83);")
        self.verticalLayout_5 = QVBoxLayout(self.iconOnly)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.label = QLabel(self.iconOnly)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/icons/icons/seal-02.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.homeIcon = QPushButton(self.iconOnly)
        self.homeIcon.setObjectName(u"homeIcon")
        self.homeIcon.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeIcon.setIcon(icon)
        self.homeIcon.setIconSize(QSize(20, 20))
        self.homeIcon.setCheckable(True)
        self.homeIcon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.homeIcon)

        self.browseIcon_2 = QPushButton(self.iconOnly)
        self.browseIcon_2.setObjectName(u"browseIcon_2")
        self.browseIcon_2.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/compass.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.browseIcon_2.setIcon(icon1)
        self.browseIcon_2.setIconSize(QSize(20, 20))
        self.browseIcon_2.setCheckable(True)
        self.browseIcon_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.browseIcon_2)

        self.reportIcon_2 = QPushButton(self.iconOnly)
        self.reportIcon_2.setObjectName(u"reportIcon_2")
        self.reportIcon_2.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/clipboard.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reportIcon_2.setIcon(icon2)
        self.reportIcon_2.setIconSize(QSize(20, 20))
        self.reportIcon_2.setCheckable(True)
        self.reportIcon_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.reportIcon_2)

        self.matchIcon = QPushButton(self.iconOnly)
        self.matchIcon.setObjectName(u"matchIcon")
        self.matchIcon.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.matchIcon.setIcon(icon3)
        self.matchIcon.setIconSize(QSize(20, 20))
        self.matchIcon.setCheckable(True)
        self.matchIcon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.matchIcon)

        self.reportIcon = QPushButton(self.iconOnly)
        self.reportIcon.setObjectName(u"reportIcon")
        self.reportIcon.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/inbox.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reportIcon.setIcon(icon4)
        self.reportIcon.setIconSize(QSize(20, 20))
        self.reportIcon.setCheckable(True)
        self.reportIcon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.reportIcon)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 528, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(14)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.settingsIcon = QPushButton(self.iconOnly)
        self.settingsIcon.setObjectName(u"settingsIcon")
        self.settingsIcon.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsIcon.setIcon(icon5)
        self.settingsIcon.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.settingsIcon)

        self.logoutIcon = QPushButton(self.iconOnly)
        self.logoutIcon.setObjectName(u"logoutIcon")
        self.logoutIcon.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutIcon.setIcon(icon6)
        self.logoutIcon.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.logoutIcon)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.iconOnly, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(247, 216, 83);")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u"icons/seal-02.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_2)
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

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(14)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 15, 5, -1)
        self.homeButton = QPushButton(self.widget_2)
        self.homeButton.setObjectName(u"homeButton")
        font1 = QFont()
        self.homeButton.setFont(font1)
        self.homeButton.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(20, 20))
        self.homeButton.setCheckable(True)
        self.homeButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.homeButton)

        self.browseButton = QPushButton(self.widget_2)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setFont(font1)
        self.browseButton.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        self.browseButton.setIcon(icon1)
        self.browseButton.setIconSize(QSize(20, 20))
        self.browseButton.setCheckable(True)
        self.browseButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.browseButton)

        self.reportButton = QPushButton(self.widget_2)
        self.reportButton.setObjectName(u"reportButton")
        self.reportButton.setFont(font1)
        self.reportButton.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        self.reportButton.setIcon(icon2)
        self.reportButton.setIconSize(QSize(20, 20))
        self.reportButton.setCheckable(True)
        self.reportButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.reportButton)

        self.matchButton = QPushButton(self.widget_2)
        self.matchButton.setObjectName(u"matchButton")
        self.matchButton.setFont(font1)
        self.matchButton.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        self.matchButton.setIcon(icon3)
        self.matchButton.setIconSize(QSize(20, 20))
        self.matchButton.setCheckable(True)
        self.matchButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.matchButton)

        self.reportButton_2 = QPushButton(self.widget_2)
        self.reportButton_2.setObjectName(u"reportButton_2")
        self.reportButton_2.setFont(font1)
        self.reportButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        self.reportButton_2.setIcon(icon4)
        self.reportButton_2.setIconSize(QSize(20, 20))
        self.reportButton_2.setCheckable(True)
        self.reportButton_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.reportButton_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 528, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(14)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settingsButton = QPushButton(self.widget_2)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setFont(font1)
        self.settingsButton.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        self.settingsButton.setIcon(icon5)
        self.settingsButton.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.settingsButton)

        self.logoutButton = QPushButton(self.widget_2)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setFont(font1)
        self.logoutButton.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        self.logoutButton.setIcon(icon6)
        self.logoutButton.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.logoutButton)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(149, 26, 31);")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_15 = QPushButton(self.widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_15.setIcon(icon7)
        self.pushButton_15.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton_15)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(279, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_17 = QPushButton(self.widget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_17.setIcon(icon8)
        self.pushButton_17.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton_17)


        self.verticalLayout_7.addWidget(self.widget)

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
        self.outisideFrame.setGeometry(QRect(20, 120, 861, 371))
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
        self.layoutWidget.setGeometry(QRect(30, 60, 821, 301))
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

        self.stackedWidget.addWidget(self.homePage)
        self.browsePage = QWidget()
        self.browsePage.setObjectName(u"browsePage")
        self.tabWidget = QTabWidget(self.browsePage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 891, 771))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lostItems = QTableWidget(self.tab)
        if (self.lostItems.columnCount() < 7):
            self.lostItems.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.lostItems.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.lostItems.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.lostItems.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.lostItems.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.lostItems.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.lostItems.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.lostItems.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.lostItems.setObjectName(u"lostItems")
        self.lostItems.setGeometry(QRect(10, 60, 861, 681))
        self.lineEdit_8 = QLineEdit(self.tab)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(10, 10, 801, 31))
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(780, 20, 16, 16))
        self.label_5.setPixmap(QPixmap(u":/icons/icons/search.svg"))
        self.label_5.setScaledContents(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lostItems_2 = QTableWidget(self.tab_2)
        if (self.lostItems_2.columnCount() < 7):
            self.lostItems_2.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.lostItems_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.lostItems_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.lostItems_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.lostItems_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.lostItems_2.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.lostItems_2.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.lostItems_2.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.lostItems_2.setObjectName(u"lostItems_2")
        self.lostItems_2.setGeometry(QRect(10, 60, 861, 681))
        self.lineEdit_13 = QLineEdit(self.tab_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(10, 10, 801, 31))
        self.lineEdit_13.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.label_24 = QLabel(self.tab_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(780, 20, 16, 16))
        self.label_24.setPixmap(QPixmap(u":/icons/icons/search.svg"))
        self.label_24.setScaledContents(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.browsePage)
        self.reportPage = QWidget()
        self.reportPage.setObjectName(u"reportPage")
        self.lineEdit_2 = QLineEdit(self.reportPage)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 150, 801, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.label_14 = QLabel(self.reportPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(300, 250, 131, 16))
        self.dateEdit = QDateEdit(self.reportPage)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(40, 320, 110, 22))
        self.dateEdit.setStyleSheet(u"")
        self.label_10 = QLabel(self.reportPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 130, 61, 16))
        self.label_12 = QLabel(self.reportPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 190, 131, 16))
        self.label_15 = QLabel(self.reportPage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 300, 131, 16))
        self.lineEdit_4 = QLineEdit(self.reportPage)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(40, 270, 101, 20))
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.label_6 = QLabel(self.reportPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(340, 30, 211, 16))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.lineEdit_5 = QLineEdit(self.reportPage)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(300, 320, 161, 20))
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.lineEdit_3 = QLineEdit(self.reportPage)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(40, 210, 801, 31))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.label_13 = QLabel(self.reportPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 250, 131, 16))
        self.lineEdit_6 = QLineEdit(self.reportPage)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(300, 270, 101, 20))
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.label_16 = QLabel(self.reportPage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(300, 300, 131, 16))
        self.lineEdit_7 = QLineEdit(self.reportPage)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(40, 380, 801, 31))
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.label_17 = QLabel(self.reportPage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(40, 360, 131, 16))
        self.label_18 = QLabel(self.reportPage)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 430, 131, 16))
        self.label_19 = QLabel(self.reportPage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 550, 101, 16))
        self.lineEdit_9 = QLineEdit(self.reportPage)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(50, 600, 251, 31))
        self.lineEdit_9.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.label_20 = QLabel(self.reportPage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(50, 580, 61, 16))
        self.label_21 = QLabel(self.reportPage)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(320, 580, 61, 16))
        self.lineEdit_10 = QLineEdit(self.reportPage)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(310, 600, 191, 31))
        self.lineEdit_10.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.lineEdit_11 = QLineEdit(self.reportPage)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(50, 640, 191, 31))
        self.lineEdit_11.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.lineEdit_12 = QLineEdit(self.reportPage)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(310, 640, 191, 31))
        self.lineEdit_12.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: white;\n"
"}")
        self.label_11 = QLabel(self.reportPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(270, 70, 61, 31))
        self.label_22 = QLabel(self.reportPage)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(490, 70, 61, 31))
        self.frame = QFrame(self.reportPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 460, 791, 80))
        self.frame.setStyleSheet(u"QFrame {\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.pushButton_21 = QPushButton(self.frame)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(370, 10, 50, 30))
        self.pushButton_21.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/arrow-down-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_21.setIcon(icon9)
        self.pushButton_21.setIconSize(QSize(20, 20))
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setAutoExclusive(True)
        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(320, 50, 151, 16))
        self.pushButton_22 = QPushButton(self.reportPage)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(340, 720, 203, 30))
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
        self.pushButton_22.setIcon(icon6)
        self.pushButton_22.setIconSize(QSize(20, 20))
        self.pushButton_23 = QPushButton(self.reportPage)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(210, 70, 50, 30))
        self.pushButton_23.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/check-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_23.setIcon(icon10)
        self.pushButton_23.setIconSize(QSize(20, 20))
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setAutoExclusive(True)
        self.pushButton_24 = QPushButton(self.reportPage)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(430, 70, 50, 30))
        self.pushButton_24.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid #2C3E50;    /* thinner border */\n"
"    border-radius: 10px;           /* small rounding */\n"
"    padding: 4px 8px;             /* top/bottom, left/right */\n"
"    background-color: #951ab;\n"
"    color: black;\n"
"    font-size: 12px;              /* smaller text */\n"
"}\n"
"")
        self.pushButton_24.setIcon(icon10)
        self.pushButton_24.setIconSize(QSize(20, 20))
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setAutoExclusive(True)
        self.stackedWidget.addWidget(self.reportPage)
        self.matchPage = QWidget()
        self.matchPage.setObjectName(u"matchPage")
        self.label_7 = QLabel(self.matchPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 390, 47, 13))
        self.stackedWidget.addWidget(self.matchPage)
        self.myreportPage = QWidget()
        self.myreportPage.setObjectName(u"myreportPage")
        self.label_8 = QLabel(self.myreportPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(390, 380, 47, 13))
        self.stackedWidget.addWidget(self.myreportPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_9 = QLabel(self.settingsPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(440, 400, 47, 13))
        self.stackedWidget.addWidget(self.settingsPage)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_15.toggled.connect(self.iconOnly.setVisible)
        self.pushButton_15.toggled.connect(self.widget_2.setHidden)
        self.homeIcon.toggled.connect(self.homeButton.setChecked)
        self.browseIcon_2.toggled.connect(self.browseButton.setChecked)
        self.reportIcon_2.toggled.connect(self.reportButton.setChecked)
        self.matchIcon.toggled.connect(self.matchButton.setChecked)
        self.reportIcon.toggled.connect(self.reportButton_2.setChecked)
        self.settingsIcon.toggled.connect(self.settingsButton.setChecked)
        self.logoutIcon.toggled.connect(self.logoutButton.setChecked)
        self.homeButton.toggled.connect(self.homeIcon.setChecked)
        self.browseButton.toggled.connect(self.browseIcon_2.setChecked)
        self.reportButton.toggled.connect(self.reportIcon_2.setChecked)
        self.matchButton.toggled.connect(self.matchIcon.setChecked)
        self.reportButton_2.toggled.connect(self.reportIcon.setChecked)
        self.settingsButton.toggled.connect(self.settingsIcon.setChecked)
        self.logoutButton.toggled.connect(self.logoutIcon.setChecked)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.homeIcon.setText("")
        self.browseIcon_2.setText("")
        self.reportIcon_2.setText("")
        self.matchIcon.setText("")
        self.reportIcon.setText("")
        self.settingsIcon.setText("")
        self.logoutIcon.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lost and Found", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse Items", None))
        self.reportButton.setText(QCoreApplication.translate("MainWindow", u"Report Item", None))
        self.matchButton.setText(QCoreApplication.translate("MainWindow", u"Match Item", None))
        self.reportButton_2.setText(QCoreApplication.translate("MainWindow", u"My Reports", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.pushButton_15.setText("")
        self.pushButton_17.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Lost and Found System!", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Let us help you find what you're looking for or return something you found.", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Recent Items", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Item Description", None))
        ___qtablewidgetitem = self.lostItems.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem1 = self.lostItems.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Brand/Model", None));
        ___qtablewidgetitem2 = self.lostItems.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.lostItems.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtablewidgetitem4 = self.lostItems.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem5 = self.lostItems.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem6 = self.lostItems.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Discoverer", None));
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"Search Item..", None))
        self.label_5.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Lost Items", None))
        ___qtablewidgetitem7 = self.lostItems_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem8 = self.lostItems_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Brand/Model", None));
        ___qtablewidgetitem9 = self.lostItems_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem10 = self.lostItems_2.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtablewidgetitem11 = self.lostItems_2.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem12 = self.lostItems_2.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem13 = self.lostItems_2.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Discoverer", None));
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"Search Item..", None))
        self.label_24.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Found Items", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Size (if applicable)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Item Details", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Brand/Model (if applicable)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Date Lost", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Lost and Found Report Form", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.lineEdit_6.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Photos", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Contact Information:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Lost Item", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Found Item", None))
        self.pushButton_21.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Drag Photos here, or Browse", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.pushButton_23.setText("")
        self.pushButton_24.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Match", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

