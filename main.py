import sys
from PyQt5 import QtWidgets
from frontend.main_window import Ui_MainWindow 
import frontend.resources_rc as resources_rc
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()