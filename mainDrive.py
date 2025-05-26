import sys
import traceback

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QDialog, QTableWidgetItem, QTableWidget, QMessageBox
from PyQt5.QtGui import QIcon
from src.frontend.mainWindow_ui import Ui_MainWindow
from src.frontend.reportItem import Ui_ReportItemDialog
from src.frontend.surrenderItem import Ui_SurrenderItemDialog
from src.backend.utils import load_functions as load
from src.backend.utils.image_utils import ImageHandler
from styles import MAIN_WINDOW_STYLE

import mysql.connector
from mysql.connector import Error
import src.backend.database.database as db
import src.backend.database.dbfunctions as dbfunctions
# import src.backend.database.dbfunctions as dbf

ROWS_PER_PAGE = 1 # change rani kung pila ka rows ang i-display per page

class MainClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Lost and Found Management System")
        self.setStyleSheet(MAIN_WINDOW_STYLE)
        self.setFixedHeight(900)
        self.setFixedWidth(1300)
        
        self.stackedWidget.setCurrentIndex(0)
        db.initialize_database()

        self.homeButton
        
        self.pageShown = 0
        self.homeButton.clicked.connect(self.goHomePage)
        self.managePersonsButton.clicked.connect(self.goManagePersonsPage)
        self.manageItemsButton.clicked.connect(self.goManageItemsPage)
        self.claimItemButton.clicked.connect(self.goClaimedItemsPage)
        self.reportItemButton.clicked.connect(self.goReportedItemsPage)
        self.surrenderItemButton.clicked.connect(self.goSurrenderedItemsPage)

        self.homeButton.setIcon(QIcon("assets/home.svg"))
        self.managePersonsButton.setIcon(QIcon("assets/persons.svg"))
        self.manageItemsButton.setIcon(QIcon("assets/items2.svg"))
        self.itemHistoryButton.setIcon(QIcon("assets/history.svg"))
        self.reportItem.setIcon(QIcon("assets/report.svg"))
        self.surrenderItem.setIcon(QIcon("assets/surrender.svg"))
        
        # Homepage Button connections
        self.reportItem.clicked.connect(self.addReportedItem)
        self.surrenderItem.clicked.connect(self.addSurrenderedItem)
        # Pagination buttons

        self.personNext.clicked.connect(self.next_person_page)
        self.personPrev.clicked.connect(self.prev_person_page)
        self.itemNextButton.clicked.connect(self.next_item_page)
        self.itemPrevButton.clicked.connect(self.prev_item_page)
        self.reportNext.clicked.connect(self.next_report_page)
        self.reportPrev.clicked.connect(self.prev_report_page)
        self.surrenderNext.clicked.connect(self.next_surrender_page)
        self.surrenderPrev.clicked.connect(self.prev_surrender_page)
        
    # Connections to add and surrender item
    def addReportedItem(self):
        reportItem = ReportItemDialog(self)
        if reportItem.exec_():
            pass

    def addSurrenderedItem(self):
        surrenderItem = SurrenderItemDialog(self)
        if surrenderItem.exec_():
            pass
    
    # PAGINATION FUNCTIONS

    def next_person_page(self):
        if (self.currentPersonPage + 1) * ROWS_PER_PAGE < dbfunctions.get_total_persons():
            self.currentPersonPage += 1
            load.load_persons(self.personTable, self.personNext, self.personPrev, self.personPageLabel, self.currentPersonPage, ROWS_PER_PAGE)

    def prev_person_page(self):
        if self.currentPersonPage > 0:
            self.currentPersonPage -= 1
            load.load_persons(self.personTable, self.personNext, self.personPrev, self.personPageLabel, self.currentPersonPage, ROWS_PER_PAGE)

    def next_item_page(self):
        if (self.currentItemPage + 1) * ROWS_PER_PAGE < dbfunctions.get_total_items():
            self.currentItemPage += 1
            load.load_items(self.itemTable, self.itemNextButton, self.itemPrevButton, self.personPageLabel_2, self.currentItemPage, ROWS_PER_PAGE)

    def prev_item_page(self):
        if self.currentItemPage > 0:
            self.currentItemPage -= 1
            load.load_items(self.itemTable, self.itemNextButton, self.itemPrevButton, self.personPageLabel_2, self.currentItemPage, ROWS_PER_PAGE)

    def next_report_page(self):
        if (self.currentReportPage + 1) * ROWS_PER_PAGE < dbfunctions.get_total_reported_items():
            self.currentReportPage += 1
            load.load_reported_items(self.reportTable, self.reportNext, self.reportPrev, self.reportPageLabel, self.currentReportPage, ROWS_PER_PAGE)

    def prev_report_page(self):
        if self.currentReportPage > 0:
            self.currentReportPage -= 1
            load.load_reported_items(self.reportTable, self.reportNext, self.reportPrev, self.reportPageLabel, self.currentReportPage, ROWS_PER_PAGE)

    def next_surrender_page(self):
        if (self.currentSurrenderPage + 1) * ROWS_PER_PAGE < dbfunctions.get_total_surrendered_items():
            self.currentSurrenderPage += 1
            load.load_surrendered_items(self.surrenderTable, self.surrenderNext, self.surrenderPrev, self.surrenederPageLabel, self.currentSurrenderPage, ROWS_PER_PAGE)

    def prev_surrender_page(self):
        if self.currentSurrenderPage > 0:
            self.currentSurrenderPage -= 1
            load.load_surrendered_items(self.surrenderTable, self.surrenderNext, self.surrenderPrev, self.surrenederPageLabel, self.currentSurrenderPage, ROWS_PER_PAGE)

    # connections of main pages

    def goHomePage(self):
        self.pageShown = 0
        self.stackedWidget.setCurrentIndex(0)

    def goManagePersonsPage(self):
        self.pageShown = 1
        self.currentPersonPage = 0  # Reset to first page
        self.stackedWidget.setCurrentIndex(1)
        load.load_persons(self.personTable, self.personNext, self.personPrev, self.personPageLabel, self.currentPersonPage, ROWS_PER_PAGE)

    # def goManagePersonsPage(self):
    #     self.pageShown = 1
    #     self.stackedWidget.setCurrentIndex(1)
    #     load.load_persons(self.personTable, self.personNext, self.personPrev, self.personPageLabel, self.currentPersonPage)

    def goManageItemsPage(self):
        self.pageshown = 2
        self.currentItemPage = 0
        self.stackedWidget.setCurrentIndex(2)
        load.load_items(self.itemTable, self.itemNextButton, self.itemPrevButton, self.personPageLabel_2, self.currentItemPage, ROWS_PER_PAGE)

    def goClaimedItemsPage(self):
        self.pageShown = 3
        self.stackedWidget.setCurrentIndex(3)

    def goReportedItemsPage(self):
        self.pageShown = 4
        self.currentReportPage = 0
        self.stackedWidget.setCurrentIndex(4)
        load.load_reported_items(self.reportTable, self.reportNext, self.reportPrev, self.reportPageLabel, self.currentReportPage, ROWS_PER_PAGE)

    def goSurrenderedItemsPage(self):
        self.pageShown = 5
        self.currentSurrenderPage = 0
        self.stackedWidget.setCurrentIndex(5)
        load.load_surrendered_items(self.surrenderTable, self.surrenderNext, self.surrenderPrev, self.surrenederPageLabel, self.currentSurrenderPage, ROWS_PER_PAGE)

class ReportItemDialog(QDialog, Ui_ReportItemDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        self.proof_id_handler = ImageHandler(self.labelImagePreview)
        self.item_image_handler = ImageHandler(self.itemImagePreview)
        self.uploadImageButton.clicked.connect(lambda: self.proof_id_handler.upload_image(self))
        self.uploadItemImageButton.clicked.connect(lambda: self.item_image_handler.upload_image(self))

        self.nextButton.clicked.connect(self.validateInputItem)
        self.confirmButton.clicked.connect(self.validateInputPerson)
        self.backButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.cancelButton.clicked.connect(self.reject)
        self.cancelButton_2.clicked.connect(self.reject)

    def itemDetailsComplete(self):
        item_name = self.itemNameEdit.text().strip().title()
        category = self.categoryEdit.text().strip().title()
        date_lost = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        location_lost = self.locationLostEdit.text().strip()
        item_desc = self.descriptionEdit.text().strip()
        status = 'Reported'

        if not (item_name and category and date_lost and location_lost and item_desc):
            QMessageBox.warning(self, "Input Error", "All fields must be filled up.")
            return False

        # Store details for later
        self.item_data = {
            "name": item_name,
            "category": category,
            "description": item_desc,
            "status": status,
            "date_lost": date_lost,
            "location_lost": location_lost
        }

        self.stackedWidget.setCurrentIndex(1)  # Move to next step
        return True
        


    def validateInputItem(self):
        if self.itemDetailsComplete():
            self.stackedWidget.setCurrentIndex(1)
    
    def validateInputPerson(self):
        first_name = self.firstNameEdit.text().strip().title()
        last_name = self.lastNameEdit.text().strip().title()
        phone_number = self.phoneNumberEdit.text().strip().replace(" ", "")
        department = self.departmentEdit.text().strip().upper()
        proof_id = self.proofIdEdit.text().strip()

        if not (first_name and last_name and phone_number and department and proof_id):
            QMessageBox.warning(self, "Input Error", "All fields must be filled up.")
            return

        try:
            # Add person
            person_id = dbfunctions.add_person(first_name, last_name, phone_number, department, proof_id)
            if not person_id:
                raise Exception("Failed to insert person.")

            # Add item + report
            item = self.item_data
            item_id = dbfunctions.add_reported_item(
                item["category"], item["name"], item["description"],
                item["date_lost"], item["location_lost"], person_id
            )

            if not item_id:
                raise Exception("Failed to insert reported item.")
            
            if self.item_image_handler.current_image_path:
                image_path = ImageHandler.save_uploaded_item_image(self.item_image_handler.current_image_path, item_id)
                dbfunctions.update_item_image_path(item_id, image_path)

            if self.proof_id_handler.current_image_path:
                proof_id_path = ImageHandler.save_uploaded_proof_id(self.proof_id_handler.current_image_path, person_id)
                dbfunctions.update_person_proof_id(person_id, proof_id_path)

            QMessageBox.information(self, "Success", "Item reported successfully.")
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        



class SurrenderItemDialog(QDialog, Ui_SurrenderItemDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        self.nextButton.clicked.connect(self.validateItemInput)
        self.confirmButton.clicked.connect(self.validatePersonInput)
        self.backButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.cancelButton.clicked.connect(self.reject)
        self.cancelButton_2.clicked.connect(self.reject)

    def goBack(self):
        self.stackedWidget.setCurrentIndex(0)

    def goToPerson(self):
        self.stackedWidget.setCurrentIndex(1)

    def itemDetailsComplete(self):
        item_name = self.itemNameEdit.text().strip().title()
        category = self.categoryEdit.text().strip().title()
        date_found = self.dateFoundEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        location_found = self.locationFoundEdit.text().strip()
        item_desc = self.descriptionEdit.text().strip()
        status = 'Surrendered'

        if not (item_name and category and date_found and location_found and item_desc):
            QMessageBox.warning(self, "Input Error", "All fields must be filled up.")
            return False

        self.item_data = {
            "name": item_name,
            "category": category,
            "description": item_desc,
            "status": status,
            "date_found": date_found,
            "location_found": location_found
        }

        self.stackedWidget.setCurrentIndex(1)
        return True

    def validateItemInput(self):
        if self.itemDetailsComplete():
            self.stackedWidget.setCurrentIndex(1)

    def validatePersonInput(self):
        first_name = self.firstNameEdit.text().strip().title()
        last_name = self.lastNameEdit.text().strip().title()
        phone_number = self.phoneNumberEdit.text().strip().replace(" ", "")
        department = self.departmentEdit.text().strip().upper()
        proof_id = self.proofIdEdit.text().strip()

        if not (first_name and last_name and phone_number and department and proof_id):
            QMessageBox.warning(self, "Input Error", "All fields must be filled up.")
            return

        try:
            # Add person
            person_id = dbfunctions.add_person(first_name, last_name, phone_number, department, proof_id)
            if not person_id:
                raise Exception("Failed to insert person.")

            # Add item + report
            item = self.item_data
            item_id = dbfunctions.add_surrendered_item(
                item["category"], item["name"], item["description"],
                item["date_found"], item["location_found"], person_id
            )

            if not item_id:
                raise Exception("Failed to insert surrendered item.")

            QMessageBox.information(self, "Success", "Item surrendered successfully.")
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec())