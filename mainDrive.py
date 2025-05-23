import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from mainWindow import Ui_MainWindow

class MainClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Lost and Found Management System")

        self.pageShown = 0
        self.homeButton.clicked.connect(self.goHomePage)
        self.managePersonsButton.clicked.connect(self.goManagePersonsPage)
        self.manageItemsButton.clicked.connect(self.goManageItemsPage)
        self.claimItemButton.clicked.connect(self.goClaimedItemsPage)
        self.reportItemButton.clicked.connect(self.goReportedItemsPage)
        self.surrenderItemButton.clicked.connect(self.goSurrenderedItemsPage)

    def goHomePage(self):
        self.pageShown = 0
        self.stackedWidget.setCurrentIndex(0)

    def goManagePersonsPage(self):
        self.pageShown = 1
        self.stackedWidget.setCurrentIndex(1)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec())