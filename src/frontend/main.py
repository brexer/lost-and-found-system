from PyQt5 import QtWidgets
import sys
from mainWindow_ui import Ui_MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    def show_page(page_widget):
        index = ui.stackedWidget.indexOf(page_widget)
        if index != -1:
            ui.stackedWidget.setCurrentIndex(index)

    ui.homeButton.clicked.connect(lambda: show_page(ui.homePage))
    ui.manageItemsButton.clicked.connect(lambda: show_page(ui.manageItemsPage))
    ui.managePersonsButton.clicked.connect(lambda: show_page(ui.managePersonsPage))
    ui.itemHistoryButton.clicked.connect(lambda: show_page(ui.reportedItems))
    ui.claimItemButton.clicked.connect(lambda: show_page(ui.claimedItems))
    ui.surrenderItemButton.clicked.connect(lambda: show_page(ui.surrenderedItems))
    ui.reportItemButton.clicked.connect(lambda: show_page(ui.reportedItems))
    MainWindow.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()