import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from src.frontend.main_window import Ui_MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Set the main window background to white and text to black
    MainWindow.setStyleSheet("background-color: white; color: black;")

    # Set SVG icons for sidebar buttons with correct button names
    ui.browseButton.setIcon(QIcon("assets/compass.svg"))
    ui.homeButton.setIcon(QIcon("assets/home.svg"))
    ui.matchButton.setIcon(QIcon("assets/clipboard.svg"))
    ui.reportButton.setIcon(QIcon("assets/search.svg"))
    ui.reportButton_2.setIcon(QIcon("assets/inbox.svg"))
    ui.settingsButton.setIcon(QIcon("assets/settings.svg"))
    ui.logoutButton.setIcon(QIcon("assets/log-out.svg"))

    # Connect sidebar buttons to pages
    ui.homeButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.homePage))
    ui.browseButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.browsePage))
    ui.matchButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.matchPage))
    ui.reportButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.reportPage))
    ui.reportButton_2.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.myreportPage))
    ui.settingsButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.settingsPage))

    MainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()