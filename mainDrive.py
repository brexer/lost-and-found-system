import sys
import traceback
import os
import re
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QDialog, QTableWidgetItem, QTableWidget, QMessageBox,QHeaderView
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QDateTime, QSize, Qt
from PyQt5 import QtWidgets

from src.frontend.mainWindow_ui import Ui_MainWindow
from src.frontend.reportItem import Ui_ReportItemDialog
from src.frontend.surrenderItem import Ui_SurrenderItemDialog
from src.frontend.updateItem import Ui_UpdateItemDialog
from src.frontend.updatePerson import Ui_UpdatePersonDialog
from src.frontend.claimPerson import Ui_ClaimPersonDialog

from src.backend.utils import recent_item_cards as ric
from src.backend.utils import load_functions as load
from src.backend.utils import match_checker as match
from src.backend.utils.image_utils import ImageHandler
from styles import MAIN_WINDOW_STYLE

import mysql.connector
from mysql.connector import Error
import src.backend.database.database as db
from src.backend.database import dbfunctions
# import src.backend.database.dbfunctions as dbf

ROWS_PER_PAGE = 2 # change rani kung pila ka rows ang i-display per page

class MainClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Lost and Found Management System")
        self.setStyleSheet(MAIN_WINDOW_STYLE)
        self.setFixedHeight(960)
        self.setFixedWidth(1310)
        
        self.stackedWidget.setCurrentIndex(0)
        db.initialize_database()

        self.match_data = []
        self.currentItemPage = 0

        self.tableSettings()

        recent_items = dbfunctions.get_recent_reported_and_surrendered(6)
        ric.load_recent_items(self.recentItemsContainer, recent_items)

        self.reportTable.cellClicked.connect(self.show_item_id_on_reported_by_click)
        self.claimTable.cellClicked.connect(self.show_person_id_on_claimed_by_click)
        self.surrenderTable.cellClicked.connect(self.show_person_id_on_surrendered_by_click)

        self.pageShown = 0
        self.homeButton.clicked.connect(self.goHomePage)
        self.managePersonsButton.clicked.connect(self.goManagePersonsPage)
        self.reviewItemsButton.setVisible(True)
        self.reviewItemsButton.clicked.connect(self.goReviewPage)
        self.claimItemButton.clicked.connect(self.goClaimedItemsPage)
        self.reportItemButton.clicked.connect(self.goReportedItemsPage)
        self.surrenderItemButton.clicked.connect(self.goSurrenderedItemsPage)

        self.homeButton.setIcon(QIcon("assets/home.svg"))
        self.homeButton.setIconSize(QSize(25, 25))  # Adjust size as needed

        self.managePersonsButton.setIcon(QIcon("assets/persons.svg"))
        self.managePersonsButton.setIconSize(QSize(25, 25))

        self.reviewItemsButton.setIcon(QIcon("assets/items2.svg"))
        self.reviewItemsButton.setIconSize(QSize(25, 25))

        self.itemHistoryButton.setIcon(QIcon("assets/history.svg"))
        self.itemHistoryButton.setIconSize(QSize(25, 25))

        self.reportItem.setIcon(QIcon("assets/report.svg"))
        self.reportItem.setIconSize(QSize(28, 28))

        self.surrenderItem.setIcon(QIcon("assets/surrender.svg"))
        self.surrenderItem.setIconSize(QSize(18, 18))
        
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
        self.claimNext.clicked.connect(self.next_claim_page)
        self.claimPrev.clicked.connect(self.prev_claim_page)

        #Claim buttons
        self.surrenderDeleteButton.setEnabled(False)
        self.surrenderDeleteButton.clicked.connect(self.claimSurrenderItem) #THIS IS THE CLAIM BUTTON
        
        # Search button
        self.searchText = ""
        self.personSearchButton.clicked.connect(self.clicked_person_search)
        self.surrenderSearchButton.clicked.connect(self.clicked_surrender_search)
        self.reportSearchButton.clicked.connect(self.clicked_report_search)
        self.claimSearchButton.clicked.connect(self.clicked_claim_search)

        #Updating item entries
        self.updateClaimButton.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.surrenderUpdateButton.setEnabled(False)
        self.reportUpdateButton.setEnabled(False)

        self.reportUpdateButton.clicked.connect(self.updateItemInput)
        self.surrenderUpdateButton.clicked.connect(self.updateItemInput)        
        self.pushButton_7.clicked.connect(self.updateItemInput)        
        self.updateClaimButton.clicked.connect(self.updateItemInput)

        #CONNECTION TO BUTTON STATES
        self.personTable.itemSelectionChanged.connect(self.update_person_button_state)
        self.claimTable.itemSelectionChanged.connect(self.update_claim_button_state)
        self.surrenderTable.itemSelectionChanged.connect(self.update_surrender_button_state)
        self.reportTable.itemSelectionChanged.connect(self.update_report_button_state)

    def tableSettings(self):
        self.personTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.personTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.personTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.personTable.verticalHeader().setVisible(False)

        self.claimTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.claimTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.claimTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.claimTable.verticalHeader().setVisible(False)

        self.surrenderTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.surrenderTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.surrenderTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.surrenderTable.verticalHeader().setVisible(False)

        self.reportTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.reportTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.reportTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.reportTable.verticalHeader().setVisible(False)

    # UPDATE BUTTON STATES
    # def update_claim_surrender_button_state(self):
    #     has_selection = self.surrenderTable.selectionModel().hasSelection()
    #     self.surrenderDeleteButton.setEnabled(has_selection)

    def update_person_button_state(self):
        has_selection = self.personTable.selectionModel().hasSelection()
        self.pushButton_7.setEnabled(has_selection)

    def update_claim_button_state(self):
        has_selection = self.claimTable.selectionModel().hasSelection()
        self.updateClaimButton.setEnabled(has_selection)

    def update_surrender_button_state(self):
        has_selection = self.surrenderTable.selectionModel().hasSelection()
        self.surrenderUpdateButton.setEnabled(has_selection)
        self.surrenderDeleteButton.setEnabled(has_selection)

    def update_report_button_state(self):
        has_selection = self.reportTable.selectionModel().hasSelection()
        self.reportUpdateButton.setEnabled(has_selection)

        # Claim functions
    def claimSurrenderItem(self):
        selectedRow = self.surrenderTable.currentRow()
        itemID = int(self.surrenderTable.item(selectedRow, 1).text())
        ClaimSurrender = ClaimPersonDialog(itemID, self)
        if ClaimSurrender.exec_():
            self.goClaimedItemsPage()
        
    # Update functions
    def updateItemInput(self):
        if self.pageShown == 1:
            if self.personTable.selectionModel().hasSelection():
                selectedRow = self.personTable.currentRow()
                personID = int(self.personTable.item(selectedRow, 1).text())
                PersonEditor = UpdatePersonEntryDialog(personID, self)
                if PersonEditor.exec_():
                    self.goManagePersonsPage
            
        elif self.pageShown == 3:
            if self.claimTable.selectionModel().hasSelection():
                selectedRow = self.claimTable.currentRow()
                itemID = int(self.claimTable.item(selectedRow, 1).text())
                ItemEditor = UpdateClaimItemDialog(itemID, self)
                if ItemEditor.exec_():
                    self.goClaimedItemsPage

        elif self.pageShown ==4:
            if self.reportTable.selectionModel().hasSelection():
                selectedRow = self.reportTable.currentRow()
                itemID = int(self.reportTable.item(selectedRow, 1).text())
                ItemEditor = UpdateReportedItemDialog(itemID, self)
                if ItemEditor.exec_():
                    self.goReportedItemsPage

        elif self.pageShown ==5:
            if self.surrenderTable.selectionModel().hasSelection():
                selectedRow = self.surrenderTable.currentRow()
                itemID = int(self.surrenderTable.item(selectedRow, 1).text())
                ItemEditor = UpdateSurrenderedItemDialog(itemID, self)
                if ItemEditor.exec_():
                    self.goSurrenderedItemsPage()
    
    # some more search functions
    def clicked_person_search(self):
        self.searchText = self.personSearchEdit.text().strip()
        self.currentPersonPage = 0
        self.update_person_page()

    def update_person_page(self):
        load.load_persons(
            self.personTable,
            self.personNext,
            self.personPrev,
            self.personPageLabel,
            self.currentPersonPage,
            ROWS_PER_PAGE,
            self.searchText
        )

    def clicked_surrender_search(self):
        self.searchText = self.surrenederSearchEdit.text().strip()
        self.currentSurrenderPage = 0
        self.update_surrender_page()

    def update_surrender_page(self):
        load.load_surrendered_items(
            self.surrenderTable,
            self.surrenderNext,
            self.surrenderPrev,
            self.surrenederPageLabel,
            self.currentSurrenderPage,
            ROWS_PER_PAGE,
            self.searchText
        )

    def clicked_report_search(self):
        self.searchText = self.reportSearchEdit.text().strip()
        self.currentReportPage = 0
        self.update_report_page()

    def update_report_page(self):
        load.load_reported_items(
            self.reportTable,
            self.reportNext,
            self.reportPrev,
            self.reportPageLabel,
            self.currentReportPage,
            ROWS_PER_PAGE,
            self.searchText
        )

    def clicked_claim_search(self):
        self.searchText = self.claimSearchEdit.text().strip()
        self.currentClaimPage = 0
        self.update_claim_page()

    def update_claim_page(self):\
        load.load_claimed_items(
            self.claimTable,
            self.claimNext,
            self.claimPrev,
            self.claimPageLabel,
            self.currentClaimPage,
            ROWS_PER_PAGE,
            self.searchText
        )

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
        search_text = self.searchText if hasattr(self, 'searchText') and self.searchText is not None else ""

        total_records = dbfunctions.get_total_persons(search_text)
        total_pages = max(1, (total_records + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE)
        if self.currentPersonPage < total_pages - 1:
            self.currentPersonPage += 1
            self.update_person_page()

    def prev_person_page(self):
        if self.currentPersonPage > 0:
            self.currentPersonPage -= 1
            self.update_person_page()

    def next_item_page(self):
        if (self.currentItemPage + 1) * ROWS_PER_PAGE < dbfunctions.get_total_items():
            total_records = len(self.match_data)
            total_pages = max(1, (total_records + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE)
        if self.currentItemPage < total_pages - 1:
            self.currentItemPage += 1
            matches = getattr(self, 'match_data', [])
            load.load_match_table(self.matchTable, self.itemNextButton, self.itemPrevButton, self.personPageLabel_2, self.currentItemPage, ROWS_PER_PAGE, matches)
            load.load_match_table(
                self.matchTable,
                self.itemNextButton,
                self.itemPrevButton,
                self.personPageLabel_2,
                self.currentItemPage,
                ROWS_PER_PAGE,
                self.match_data
            )

    def prev_item_page(self):
        if self.currentItemPage > 0:
            self.currentItemPage -= 1
            matches = getattr(self, 'match_data', [])
            load.load_match_table(self.matchTable, self.itemNextButton, self.itemPrevButton, self.personPageLabel_2, self.currentItemPage, ROWS_PER_PAGE, matches)
            load.load_match_table(
                self.matchTable,
                self.itemNextButton,
                self.itemPrevButton,
                self.personPageLabel_2,
                self.currentItemPage,
                ROWS_PER_PAGE,
                self.match_data
            )

    def next_report_page(self):
        search_text = self.searchText if hasattr(self, 'searchText') and self.searchText is not None else ""

        total_records = dbfunctions.get_total_reported_items(search_text)
        total_pages = max(1, (total_records + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE)
        if self.currentReportPage < total_pages - 1:
            self.currentReportPage += 1
            self.update_report_page()

    def prev_report_page(self):
        if self.currentReportPage > 0:
            self.currentReportPage -= 1
            self.update_report_page()

    def next_surrender_page(self):
        search_text = self.searchText if hasattr(self, 'searchText') and self.searchText is not None else ""

        total_records = dbfunctions.get_total_surrendered_items(search_text)
        total_pages = max(1, (total_records + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE)

        if self.currentSurrenderPage < total_pages - 1:
            self.currentSurrenderPage += 1
            self.update_surrender_page()

    def prev_surrender_page(self):
        if self.currentSurrenderPage > 0:
            self.currentSurrenderPage -= 1
            self.update_surrender_page()

    def next_claim_page(self):
        search_text = self.searchText if hasattr(self, 'searchText') and self.searchText is not None else ""

        total_records = dbfunctions.get_total_claimed_items(search_text)
        total_pages = max(1, (total_records + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE)

        if self.currentClaimPage < total_pages - 1:
            self.currentClaimPage += 1
            self.update_claim_page()

    def prev_claim_page(self):
        if self.currentClaimPage > 0:
            self.currentClaimPage -= 1
            self.update_claim_page()

    # connections of main pages

    def goHomePage(self):
        self.pageShown = 0
        self.stackedWidget.setCurrentIndex(0)

    def goManagePersonsPage(self):
        self.pageShown = 1
        self.searchText = ""
        self.currentPersonPage = 0
        self.stackedWidget.setCurrentIndex(1)
        load.load_persons(self.personTable, self.personNext, self.personPrev, self.personPageLabel, self.currentPersonPage, ROWS_PER_PAGE)
        self.personTable.horizontalHeader().setStretchLastSection(True)
        self.personTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # def goManagePersonsPage(self):
    #     self.pageShown = 1
    #     self.stackedWidget.setCurrentIndex(1)
    #     load.load_persons(self.personTable, self.personNext, self.personPrev, self.personPageLabel, self.currentPersonPage)

    def goReviewPage(self):
        self.currentItemPage = 0
        matches = self.match_data
        load.load_match_table(self.matchTable, self.itemNextButton, self.itemPrevButton, self.personPageLabel_2, self.currentItemPage, ROWS_PER_PAGE, matches)
        load.load_match_table(
            self.matchTable,
            self.itemNextButton,
            self.itemPrevButton,
            self.personPageLabel_2,
            self.currentItemPage,
            ROWS_PER_PAGE,
            matches
        )
        self.pageshown = 2
        self.currentItemPage = 0
        self.stackedWidget.setCurrentIndex(2)

    def goClaimedItemsPage(self):
        self.pageShown = 3
        self.currentClaimPage = 0
        self.stackedWidget.setCurrentIndex(3)
        load.load_claimed_items(self.claimTable, self.claimNext, self.claimPrev, self.claimPageLabel, self.currentClaimPage, ROWS_PER_PAGE)
        self.claimTable.horizontalHeader().setStretchLastSection(True)
        self.claimTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def goReportedItemsPage(self):
        self.pageShown = 4
        self.searchText = ""
        self.currentReportPage = 0
        self.stackedWidget.setCurrentIndex(4)
        load.load_reported_items(self.reportTable, self.reportNext, self.reportPrev, self.reportPageLabel, self.currentReportPage, ROWS_PER_PAGE)
        self.reportTable.horizontalHeader().setStretchLastSection(True)
        self.reportTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def goSurrenderedItemsPage(self):
        self.pageShown = 5
        self.searchText = ""
        self.currentSurrenderPage = 0
        self.stackedWidget.setCurrentIndex(5)
        load.load_surrendered_items(self.surrenderTable, self.surrenderNext, self.surrenderPrev, self.surrenederPageLabel, self.currentSurrenderPage, ROWS_PER_PAGE)
        self.surrenderTable.horizontalHeader().setStretchLastSection(True)
        self.surrenderTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def show_item_id_on_reported_by_click(self, row, column):
        if column == 8:
            person_item = self.reportTable.item(row, column)
            if person_item:
                person_id = person_item.data(Qt.UserRole)
            if person_id:
                QMessageBox.information(self, "Person ID", f"The Person's ID is: {person_id}")
            else:
                QMessageBox.warning(self, "No Data", "No Person ID found for this entry.")

    def show_person_id_on_claimed_by_click(self, row, column):
        if column == 8:
            person_item = self.claimTable.item(row, column)
            if person_item:
                person_id = person_item.data(Qt.UserRole)
                if person_id:
                    QMessageBox.information(self, "Person ID", f"The Claimer's Person ID is: {person_id}")
                else:
                    QMessageBox.warning(self, "No Data", "No Person ID found for this entry.")

    def show_person_id_on_surrendered_by_click(self, row, column):
        if column == 8:
            person_item = self.surrenderTable.item(row, column)
            if person_item:
                person_id = person_item.data(Qt.UserRole)
                if person_id:
                    QMessageBox.information(self, "Person ID", f"The Surrenderer's Person ID is: {person_id}")
                else:
                    QMessageBox.warning(self, "No Data", "No Person ID found for this entry.")

class ReportItemDialog(QDialog, Ui_ReportItemDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        self.proof_id_handler = ImageHandler(self.proofImagePreview)
        self.item_image_handler = ImageHandler(self.itemImagePreview)
        self.uploadProofButton.clicked.connect(lambda: self.proof_id_handler.upload_image(self))
        self.itemImageButton.clicked.connect(lambda: self.item_image_handler.upload_image(self))

        self.dateLostEdit.setMaximumDateTime(QDateTime.currentDateTime())
        self.dateLostEdit.setDateTime(QDateTime.currentDateTime())

        self.nextButton.clicked.connect(self.validateInputItem)
        self.confirmButton.clicked.connect(self.validateInputPerson)
        self.backButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.cancelButton.clicked.connect(self.reject)
        self.cancelButton_2.clicked.connect(self.reject)

    def itemDetailsComplete(self):
        item_name = self.itemNameEdit.text().strip().title()
        category = self.comboBox_2.currentText().strip().title()
        date_lost = self.dateLostEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
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

        if not (first_name and last_name and phone_number and department):
            QMessageBox.warning(self, "Input Error", "All fields must be filled up.")
            return

        name_pattern = r"^[A-Za-z ]+$"
        if not all([
            re.fullmatch(name_pattern, first_name),
            re.fullmatch(name_pattern, last_name),
            re.fullmatch(name_pattern, department)
        ]):
            QMessageBox.warning(self, "Input Error", "Names and department must contain only letters and spaces.")
            return
        
        if not re.fullmatch(r"09\d{9}", phone_number):
            QMessageBox.warning(self, "Input Error", "Please input a valid phone number.")
            return
        
        try:
            # Add person
            person_id = dbfunctions.add_person(first_name, last_name, phone_number, department)
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

        self.proof_id_handler = ImageHandler(self.proofImagePreview)
        self.item_image_handler = ImageHandler(self.itemImagePreview)
        self.proofImageButton.clicked.connect(lambda: self.proof_id_handler.upload_image(self))
        self.itemImageButton.clicked.connect(lambda: self.item_image_handler.upload_image(self))

        self.dateFoundEdit.setMaximumDateTime(QDateTime.currentDateTime())
        self.dateFoundEdit.setDateTime(QDateTime.currentDateTime())

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
        category = self.comboBox_2.currentText().strip().title()
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
        department = self.departmentEdit_2.text().strip().upper()

        item = self.item_data
        category = item["category"]
        date_found = item.get("date_found") 

        matches = match.check_reported_matches(category, date_found)

        if not (first_name and last_name and phone_number and department):
            QMessageBox.warning(self, "Input Error", "All fields must be filled up.")
            return
        
        if not all([first_name.isalpha(), last_name.isalpha(), department.isalpha()]):
            QMessageBox.warning(self, "Input Error", "Please input valid data.")
            return
        
        if not re.fullmatch(r"09\d{9}", phone_number):
            QMessageBox.warning(self, "Input Error", "Please input a valid phone number.")
            return

        try:
            person_id = dbfunctions.get_existing_person_id(first_name, last_name, department)

            if person_id:
                print(f"Existing person found: ID = {person_id}")
            else:
                person_id = dbfunctions.add_person(first_name, last_name, phone_number, department)
                if not person_id:
                    raise Exception("Failed to insert person.")

            item_id = dbfunctions.add_surrendered_item(
                item["category"], item["name"], item["description"],
                item["date_found"], item["location_found"], person_id
            )

            if not item_id:
                raise Exception("Failed to insert surrendered item.")

            if self.item_image_handler.current_image_path:
                image_path = ImageHandler.save_uploaded_item_image(self.item_image_handler.current_image_path, item_id)
                dbfunctions.update_item_image_path(item_id, image_path)

            if self.proof_id_handler.current_image_path:
                proof_id_path = ImageHandler.save_uploaded_proof_id(self.proof_id_handler.current_image_path, person_id)
                dbfunctions.update_person_proof_id(person_id, proof_id_path)

            if matches:
                self.parent().match_data = matches
                self.parent().reviewItemsButton.setVisible(True)
                QMessageBox.information(self, "Match Found", "Possible match(es) found. Click 'Review Matches' to view.")
            else:
                self.parent().match_data = []
                self.parent().reviewItemsButton.setVisible(False)

            QMessageBox.information(self, "Success", "Item surrendered successfully.")
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

class UpdateSurrenderedItemDialog(QDialog, Ui_UpdateItemDialog):
    def __init__(self, itemID, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.itemID = itemID

        self.loadItemData()

        self.item_image_handler = ImageHandler(self.itemImagePreview)
        self.pushButton.clicked.connect(lambda: self.item_image_handler.upload_image(self))
        
        self.cancelButton.clicked.connect(self.reject)
        self.confirmButton.clicked.connect(self.validateItemInput)

    def loadItemData(self):
        conn = db.create_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT Name, Category, DateFound, LocationFound, Description, ImagePath FROM Items WHERE ItemID = %s", (self.itemID,))
            row = cursor.fetchone()
            if row:
                item_name, category, date_found, location, description, image_path = row

                self.itemNameEdit.setText(item_name)
                index = self.categoryComboBox.findText(category)
                if index != -1:
                    self.categoryComboBox.setCurrentIndex(index)
                dt = QDateTime.fromString(str(date_found), "yyyy-MM-dd HH:mm:ss")
                self.dateTimeEdit.setDateTime(dt)
                self.locationEdit.setText(location)
                self.descriptionEdit.setText(description)

                if image_path and os.path.exists(image_path):
                    pixmap = QPixmap(image_path).scaled(
                        self.itemImagePreview.size(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                    self.itemImagePreview.setPixmap(pixmap)
            else:
                QMessageBox.warning(self, "Error", "Item not found.")
                self.reject()
        finally:
            conn.close()

    def updateItemInput(self):
        item_name = self.itemNameEdit.text().strip().title()
        category = self.categoryComboBox.currentText()
        date_found = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        location_found = self.locationEdit.text().strip().title()
        item_desc = self.descriptionEdit.text().strip()

        return {
            "Name": item_name,
            "Category": category,
            "DateFound": date_found,
            "LocationFound": location_found,
            "Description": item_desc
        }

    def validateItemInput(self):
        data = self.updateItemInput()

        if not all(data.values()):
            QMessageBox.warning(self, "Validation Error", "Please fill in all fields.")
            return

        image_path = None
        if self.item_image_handler.current_image_path:
            image_path = ImageHandler.save_uploaded_item_image(
                self.item_image_handler.current_image_path, self.itemID
            )

        try:
            conn = db.create_connection()
            cursor = conn.cursor()

            # Update with or without image depending on change
            if image_path:
                cursor.execute("""
                    UPDATE Items
                    SET Name = %s, Category = %s, DateFound = %s,
                        LocationFound = %s, Description = %s, ImagePath = %s
                    WHERE ItemID = %s
                """, (
                    data["Name"], data["Category"], data["DateFound"],
                    data["LocationFound"], data["Description"],
                    image_path, self.itemID
                ))
            else:
                cursor.execute("""
                    UPDATE Items
                    SET Name = %s, Category = %s, DateFound = %s,
                        LocationFound = %s, Description = %s
                    WHERE ItemID = %s
                """, (
                    data["Name"], data["Category"], data["DateFound"],
                    data["LocationFound"], data["Description"], self.itemID
                ))

            conn.commit()
            QMessageBox.information(self, "Success", "Item updated successfully.")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
        finally:
            conn.close()

class UpdateReportedItemDialog(QDialog, Ui_UpdateItemDialog):
    def __init__(self, itemID, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.itemID = itemID

        self.loadItemData()

        self.item_image_handler = ImageHandler(self.itemImagePreview)
        self.pushButton.clicked.connect(lambda: self.item_image_handler.upload_image(self))

        self.cancelButton.clicked.connect(self.reject)
        self.confirmButton.clicked.connect(self.validateItemInput)

    def loadItemData(self):
        conn = db.create_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT Name, Category, DateLost, LocationLost, Description, ImagePath FROM Items WHERE ItemID = %s", (self.itemID,))
            row = cursor.fetchone()
            if row:
                item_name, category, date_lost, location, description, image_path = row

                self.itemNameEdit.setText(item_name)
                index = self.categoryComboBox.findText(category)
                if index != -1:
                    self.categoryComboBox.setCurrentIndex(index)
                dt = QDateTime.fromString(str(date_lost), "yyyy-MM-dd HH:mm:ss")
                self.dateTimeEdit.setDateTime(dt)
                self.locationEdit.setText(location)
                self.descriptionEdit.setText(description)

                if image_path and os.path.exists(image_path):
                    pixmap = QPixmap(image_path).scaled(
                        self.itemImagePreview.size(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                    self.itemImagePreview.setPixmap(pixmap)

            else:
                QMessageBox.warning(self, "Error", "Item not found.")
                self.reject()
        finally:
            conn.close()

    def updateItemInput(self):
        item_name = self.itemNameEdit.text().strip().title()
        category = self.categoryComboBox.currentText()
        date_lost = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        location_lost = self.locationEdit.text().strip().title()
        item_desc = self.descriptionEdit.text().strip()

        return {
            "Name": item_name,
            "Category": category,
            "DateLost": date_lost,
            "LocationLost": location_lost,
            "Description": item_desc
        }

    def validateItemInput(self):
        data = self.updateItemInput()
        
        # Basic validation
        if not all(data.values()):
            QMessageBox.warning(self, "Validation Error", "Please fill in all fields.")
            return
        
        image_path = None
        if self.item_image_handler.current_image_path:
            image_path = ImageHandler.save_uploaded_item_image(
                self.item_image_handler.current_image_path, self.itemID
            )

        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            
            if image_path:
                cursor.execute("""
                    UPDATE Items
                    SET Name = %s, Category = %s, DateLost = %s, LocationLost = %s, Description = %s, ImagePath = %s
                    WHERE ItemID = %s
                """, (
                    data["Name"], data["Category"], data["DateLost"], data["LocationLost"], data["Description"], image_path, self.itemID
                ))
            else:
                cursor.execute("""
                    UPDATE Items
                    SET Name = %s, Category = %s, DateLost = %s, LocationLost = %s, Description = %s
                    WHERE ItemID = %s
                """, (
                    data["Name"], data["Category"], data["DateLost"], data["LocationLost"], data["Description"], self.itemID
                ))
            
            conn.commit()
            QMessageBox.information(self, "Success", "Item updated successfully.")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
        finally:
            conn.close()

class UpdatePersonEntryDialog(QDialog, Ui_UpdatePersonDialog):
    def __init__(self, personID, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.personID = personID

        self.loadPersonData()

        self.proof_id_handler = ImageHandler(self.proofImagePreview)
        self.uploadImageButton.clicked.connect(lambda: self.proof_id_handler.upload_image(self))

        self.cancelButton.clicked.connect(self.reject)
        self.confirmButton.clicked.connect(self.validatePersonInput)

    def loadPersonData(self):
        conn = db.create_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT FirstName, LastName, PhoneNumber, Department, ProofID FROM Persons WHERE PersonID = %s", (self.personID,))
            row = cursor.fetchone()
            if row:
                first_name, last_name, phone_number, department, proof_id = row

                self.firstNameEdit.setText(first_name)
                self.lastNameEdit.setText(last_name)
                self.phoneNumberEdit.setText(phone_number)
                self.departmentEdit.setText(department)

                if proof_id and os.path.exists(proof_id):
                    pixmap = QPixmap(proof_id).scaled(
                        self.proofImagePreview.size(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                    self.proofImagePreview.setPixmap(pixmap)
            else:
                QMessageBox.warning(self, "Error", "Item not found.")
                self.reject()
        finally:
            conn.close()

    def updatePersonInput(self):
        first_name = self.firstNameEdit.text().strip().title()
        last_name = self.lastNameEdit.text().strip().title()
        phone_number = self.phoneNumberEdit.text().strip()
        department = self.departmentEdit.text().strip().upper().replace(" ","")

        return {
            "FirstName": first_name,
            "LastName": last_name,
            "PhoneNumber": phone_number,
            "Department": department
        }


    def validatePersonInput(self):
        data = self.updatePersonInput()
        
        if not all(data.values()):
            QMessageBox.warning(self, "Validation Error", "Please fill in all fields.")
            return
        
        if not all([data["FirstName"].isalpha(), data["LastName"].isalpha(), data["Department"].isalpha()]):
            QMessageBox.warning(self, "Input Error", "Please input valid data.")
            return
        
        if not re.fullmatch(r"09\d{9}", data["PhoneNumber"]):
            QMessageBox.warning(self, "Input Error", "Please input a valid phone number.")
            return
        
        proof_id = None
        if self.proof_id_handler.current_image_path: proof_id = ImageHandler.save_uploaded_proof_id(self.proof_id_handler.current_image_path, self.personID)

        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Persons
                SET FirstName = %s, LastName = %s, PhoneNumber = %s, Department = %s
                WHERE PersonID = %s
            """, (data["FirstName"], data["LastName"], data["PhoneNumber"], data["Department"], self.personID))
            conn.commit()
            QMessageBox.information(self, "Success", "Person entry updated successfully.")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
        finally:
            conn.close()

class UpdateClaimItemDialog(QDialog, Ui_UpdateItemDialog):
    def __init__(self, itemID, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.itemID = itemID

        self.loadItemData()

        self.item_image_handler = ImageHandler(self.itemImagePreview)
        self.pushButton.clicked.connect(lambda: self.item_image_handler.upload_image(self))

        self.cancelButton.clicked.connect(self.reject)
        self.confirmButton.clicked.connect(self.validateItemInput)

    def loadItemData(self):
        conn = db.create_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT Name, Category, DateFound, LocationFound, Description, ImagePath FROM Items WHERE ItemID = %s", (self.itemID,))
            row = cursor.fetchone()
            if row:
                item_name, category, date_found, location, description, image_path = row

                self.itemNameEdit.setText(item_name)
                index = self.categoryComboBox.findText(category)
                if index != -1:
                    self.categoryComboBox.setCurrentIndex(index)
                dt = QDateTime.fromString(str(date_found), "yyyy-MM-dd HH:mm:ss")
                self.dateTimeEdit.setDateTime(dt)
                self.locationEdit.setText(location)
                self.descriptionEdit.setText(description)

                if image_path and os.path.exists(image_path):
                    pixmap = QPixmap(image_path).scaled(
                        self.itemImagePreview.size(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                    self.itemImagePreview.setPixmap(pixmap)
            else:
                QMessageBox.warning(self, "Error", "Item not found.")
                self.reject()
        finally:
            conn.close()

    def updateItemInput(self):
        item_name = self.itemNameEdit.text().strip().title()
        category = self.categoryComboBox.currentText()
        date_found = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        location_found = self.locationEdit.text().strip().title()
        item_desc = self.descriptionEdit.text().strip()

        return {
            "Name": item_name,
            "Category": category,
            "DateFound": date_found,
            "LocationFound": location_found,
            "Description": item_desc
        }

    def validateItemInput(self):
        data = self.updateItemInput()
        
        if not all(data.values()):
            QMessageBox.warning(self, "Validation Error", "Please fill in all fields.")
            return

        image_path = None
        if self.item_image_handler.current_image_path:
            image_path = ImageHandler.save_uploaded_item_image(
                self.item_image_handler.current_image_path, self.itemID
            )

        try:
            conn = db.create_connection()
            cursor = conn.cursor()

            if image_path:
                cursor.execute("""
                    UPDATE Items
                    SET Name = %s, Category = %s, DateFound = %s, LocationFound = %s, Description = %s, ImagePath = %s
                    WHERE ItemID = %s
                """, (
                    data["Name"], data["Category"], data["DateFound"], data["LocationFound"], data["Description"], image_path, self.itemID
                ))
            else:
                cursor.execute("""
                    UPDATE Items
                    SET Name = %s, Category = %s, DateFound = %s, LocationFound = %s, Description = %s
                    WHERE ItemID = %s
                """, (
                    data["Name"], data["Category"], data["DateFound"], data["LocationFound"], data["Description"], self.itemID
                ))

            conn.commit()
            QMessageBox.information(self, "Success", "Item updated successfully.")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
        finally:
            conn.close()

class ClaimPersonDialog(QDialog, Ui_ClaimPersonDialog):
    def __init__(self, itemID, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.itemID = itemID

        self.proof_id_handler = ImageHandler(self.proofImagePreview)
        self.uploadImageButton.clicked.connect(lambda: self.proof_id_handler.upload_image(self))

        self.cancelButton.clicked.connect(self.reject)
        self.confirmButton.clicked.connect(self.validatePersonInput)

    def validatePersonInput(self):
        first_name = self.firstNameEdit.text().strip().title()
        last_name = self.lastNameEdit.text().strip().title()
        phone_number = self.phoneNumberEdit.text().strip().replace(" ", "")
        department = self.departmentEdit.text().strip().upper()

        if not (first_name and last_name and phone_number and department):
            QMessageBox.warning(self, "Input Error", "All fields must be filled up.")
            return
        
        if not all([first_name.isalpha(), last_name.isalpha(), department.isalpha()]):
            QMessageBox.warning(self, "Input Error", "Please input valid data.")
            return
        
        if not re.fullmatch(r"09\d{9}", phone_number):
            QMessageBox.warning(self, "Input Error", "Please input a valid phone number.")
            return

        try:
            # Check for existing person
            existing_person_id = dbfunctions.get_existing_person_id(first_name, last_name, department)

            if existing_person_id:
                person_id = existing_person_id
            else:
                # Add new person
                person_id = dbfunctions.add_person(first_name, last_name, phone_number, department)
                if not person_id:
                    raise Exception("Failed to insert person.")

                # Save proof ID if provided
                if self.proof_id_handler.current_image_path:
                    proof_id_path = ImageHandler.save_uploaded_proof_id(self.proof_id_handler.current_image_path, person_id)
                    dbfunctions.update_person_proof_id(person_id, proof_id_path)

            # Get current timestamp
            date_claimed = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Attempt to claim the item
            success = dbfunctions.claim_item(self.itemID, date_claimed, person_id)
            if not success:
                QMessageBox.warning(self, "Claim Error", "Item is already claimed or invalid.")
                return

            QMessageBox.information(self, "Success", "Item claimed successfully.")
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec())