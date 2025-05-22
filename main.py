import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from testt.main_window import Ui_MainWindow
from src.backend.database import dbfunctions

def load_reported_items(table_widget):
    all_items = dbfunctions.get_all_items()
    reported_items = [item for item in all_items if item[4] == "Unclaimed"]

    table = table_widget
    table.setRowCount(0)
    table.setColumnCount(8)
    table.setHorizontalHeaderLabels([
        "Item ID", "Category", "Name", "Description", "Status", "Location", "Date", "Reported By"
    ])
    
    for row_num, item in enumerate(reported_items):
        table.insertRow(row_num)
        for col, value in enumerate(item):
            table.setItem(row_num, col, QtWidgets.QTableWidgetItem(str(value)))


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    load_reported_items(ui.tableWidget)

    # Set the main window background to white and text to black
    MainWindow.setStyleSheet("background-color: white; color: black;")

    # Connect sidebar buttons to pages
    ui.homeButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.homePage))
    ui.lostButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.ReportedItems))
    ui.foundButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.SurrenderedItems))
    ui.claimedButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.ClaimedItems))
    ui.reportButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.myreportPage))
    ui.settingsButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.ManagePersons))

    MainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()