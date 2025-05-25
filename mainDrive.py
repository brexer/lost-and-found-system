import sys
import traceback

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QDialog, QTableWidgetItem, QTableWidget
from src.frontend.mainWindow_ui import Ui_MainWindow
from src.frontend.reportItem import Ui_ReportItemDialog
from src.frontend.surrenderItem import Ui_SurrenderItemDialog
from src.backend.utils import load_functions as load
from styles import MAIN_WINDOW_STYLE

import mysql.connector
from mysql.connector import Error
import src.backend.database.database as db
import src.backend.database.dbfunctions as dbf
# import src.backend.database.dbfunctions as dbf


class MainClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Lost and Found Management System")
        self.setStyleSheet(MAIN_WINDOW_STYLE)

        db.initialize_database()


        self.pageShown = 0
        self.homeButton.clicked.connect(self.goHomePage)
        self.managePersonsButton.clicked.connect(self.goManagePersonsPage)
        self.manageItemsButton.clicked.connect(self.goManageItemsPage)
        self.claimItemButton.clicked.connect(self.goClaimedItemsPage)
        self.reportItemButton.clicked.connect(self.goReportedItemsPage)
        self.surrenderItemButton.clicked.connect(self.goSurrenderedItemsPage)

        # Homepage Button connections
        self.reportItem.clicked.connect(self.addReportedItem)

    # Connections to add and surrender item
    def addReportedItem(self):
        reportItem = ReportItemDialog(self)
        if reportItem.exec_():
            pass

    def addSurrenderedItem(self):
        surrenderItem = SurrenderItemDialog(self)
        if surrenderItem.exec_():
            pass

    # connections of main pages

    def goHomePage(self):
        self.pageShown = 0
        self.stackedWidget.setCurrentIndex(0)

    def goManagePersonsPage(self):
        self.pageShown = 1
        self.stackedWidget.setCurrentIndex(1)
        load.load_persons(self.personTable)

    def goManageItemsPage(self):
        self.pageshown = 2
        self.stackedWidget.setCurrentIndex(2)

    def goClaimedItemsPage(self):
        self.pageShown = 3
        self.stackedWidget.setCurrentIndex(3)

    def goReportedItemsPage(self):
        self.pageShown = 4
        self.stackedWidget.setCurrentIndex(4)

    def goSurrenderedItemsPage(self):
        self.pageShown = 5
        self.stackedWidget.setCurrentIndex(5)

class ReportItemDialog(QDialog, Ui_ReportItemDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        self.nextButton.clicked.connect(self.goToPerson)
        self.confirmButton.clicked.connect(self.validateInput)
        self.backButton.clicked.connect(self.goBack)

        self.cancelButton.clicked.connect(self.reject)
        self.cancelButton_2.clicked.connect(self.reject)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(0)

    def goToPerson(self):
        self.stackedWidget.setCurrentIndex(1)

    def validateInput(self):
        pass

class SurrenderItemDialog(QDialog, Ui_SurrenderItemDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        self.nextButton.clicked.connect(self.goToPerson)
        self.confirmButton.clicked.connect(self.validateInput)
        self.backButton.clicked.connect(self.goBack)

        self.cancelButton.clicked.connect(self.reject)
        self.cancelButton_2.clicked.connect(self.reject)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(0)

    def goToPerson(self):
        self.stackedWidget.setCurrentIndex(1)

    def validateInput(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec())