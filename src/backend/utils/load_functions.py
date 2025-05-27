from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QLabel
from src.backend.database import dbfunctions
from src.backend.utils import match_checker as match
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from src.backend.utils.image_utils import ClickableLabel
import os

def load_reported_items(reportTable, reportNext, reportPrev, reportPageLabel, currentReportPage, page_size, search_text=""):
    reported_items, total_records = dbfunctions.get_all_reported_items(currentReportPage, page_size, search_text)
    total_pages = max(1, (total_records + page_size - 1) // page_size)

    table = reportTable
    table.setRowCount(0)
    table.setColumnCount(9)
    table.setHorizontalHeaderLabels([
        "Image", "Item ID", "Category", "Name", "Description", "Status", "Location", "Date", "Reported By"
    ])

    for row_num, item in enumerate(reported_items):
        table.insertRow(row_num)

        image_path = item["ImagePath"]
        abs_path = os.path.abspath(image_path) if image_path else None
        display_image_in_cell(table, row_num, abs_path)

        values = [
            item["ItemID"],
            item["Category"],
            item["Name"],
            item["Description"],
            item["Status"],
            item["LocationLost"],
            item["DateLost"],
            item["ReportedBy"]
        ]

        for col, value in enumerate(values):
            table.setItem(row_num, col + 1, QTableWidgetItem(str(value)))

    reportPageLabel.setText(f"Page {currentReportPage + 1} of {total_pages}")
    reportPrev.setEnabled(currentReportPage > 0)
    reportNext.setEnabled(currentReportPage < total_pages - 1)

    table.verticalHeader().setDefaultSectionSize(70)
    table.setColumnWidth(0, 80)

def load_surrendered_items(surrenderTable, surrenderNext, surrenderPrev, surrenderPageLabel, currentSurrenderPage, page_size, search_text=""):
    surrendered_items, total_records = dbfunctions.get_all_surrendered_items(currentSurrenderPage, page_size, search_text)
    total_pages = max(1, (total_records + page_size - 1) // page_size)

    table = surrenderTable
    table.setRowCount(0)
    table.setColumnCount(9)
    table.setHorizontalHeaderLabels([
        "Image", "Item ID", "Category", "Name", "Description", "Status", "Location", "Date", "Surrendered By"
    ])

    for row_num, item in enumerate(surrendered_items):
        table.insertRow(row_num)

        image_path = item["ImagePath"]
        abs_path = os.path.abspath(image_path) if image_path else None
        display_image_in_cell(table, row_num, abs_path)

        values = [
            item.get("ItemID", ""),
            item.get("Category", ""),
            item.get("Name", ""),
            item.get("Description", ""),
            item.get("Status", ""),
            item.get("LocationFound", ""),
            item.get("DateFound", ""),
            item.get("SurrenderedBy", "")
        ]

        for col, value in enumerate(values):
            table.setItem(row_num, col + 1, QTableWidgetItem(str(value)))

    surrenderPageLabel.setText(f"Page {currentSurrenderPage + 1} of {total_pages}")
    surrenderPrev.setEnabled(currentSurrenderPage > 0)
    surrenderNext.setEnabled(currentSurrenderPage < total_pages - 1)

    table.verticalHeader().setDefaultSectionSize(70)
    table.setColumnWidth(0, 80)

def load_claimed_items(claimTable, claimNext, claimPrev, claimPageLabel, currentClaimPage, page_size, search_text=""):
    claimed_items, total_records = dbfunctions.get_all_claimed_items(currentClaimPage, page_size, search_text)
    total_pages = max(1, (total_records + page_size - 1) // page_size)

    table = claimTable
    table.setRowCount(0)
    table.setColumnCount(9)
    table.setHorizontalHeaderLabels([
        "Image", "Item ID", "Category", "Name", "Description", "Status", "Location", "Date", "Claimed By"
    ])

    for row_num, item in enumerate(claimed_items):
        table.insertRow(row_num)

        image_path = item["ImagePath"]
        abs_path = os.path.abspath(image_path) if image_path else None
        display_image_in_cell(table, row_num, abs_path)

        values = [
            item.get("ItemID", ""),
            item.get("Category", ""),
            item.get("Name", ""),
            item.get("Description", ""),
            item.get("Status", ""),
            item.get("LocationFound", ""),
            item.get("DateClaimed", ""),
            item.get("ClaimedBy", "")
        ]

        for col, value in enumerate(values):
            table.setItem(row_num, col + 1, QTableWidgetItem(str(value)))


    claimPageLabel.setText(f"Page {currentClaimPage + 1} of {total_pages}")
    claimPrev.setEnabled(currentClaimPage > 0)
    claimNext.setEnabled(currentClaimPage < total_pages - 1)

    table.verticalHeader().setDefaultSectionSize(70)
    table.setColumnWidth(0, 80)

def load_persons(personTable, personNext, personPrev, personPageLabel, currentPersonPage, page_size, search_text=""):
    persons, total_records = dbfunctions.get_all_persons(currentPersonPage, page_size, search_text)
    total_pages = max(1, (total_records + page_size - 1) // page_size)

    table = personTable
    table.setRowCount(0)
    table.setColumnCount(6)
    table.setHorizontalHeaderLabels([
        "Proof", "Person ID", "First Name", "Last Name", "Phone Number", "Department"
    ])

    for row_num, person in enumerate(persons):
        table.insertRow(row_num)

        # === Display ProofID image ===
        image_path = person[5]  # ProofID column (image path)
        abs_path = os.path.abspath(image_path) if image_path else None
        display_image_in_cell(table, row_num, abs_path)

        # === Add person details ===
        for col in range(5):  # 0 to 4 (PersonID to Department)
            table.setItem(row_num, col + 1, QTableWidgetItem(str(person[col])))

    personPageLabel.setText(f"Page {currentPersonPage + 1} of {total_pages}")
    personPrev.setEnabled(currentPersonPage > 0)
    personNext.setEnabled(currentPersonPage < total_pages - 1)

    table.verticalHeader().setDefaultSectionSize(70)
    table.setColumnWidth(0, 80)
    
def load_items(itemTable, itemNext, itemPrev, itemPageLabel, currentItemPage, page_size):
    items, total_records = dbfunctions.get_all_items(currentItemPage, page_size)
    total_pages = max(1, (total_records + page_size - 1) // page_size)

    table = itemTable
    table.setRowCount(0)
    table.setColumnCount(6)

    for row_num, item in enumerate(items):
        table.insertRow(row_num)
        for col, value in enumerate(item):
            table.setItem(row_num, col, QtWidgets.QTableWidgetItem(str(value)))

    itemPageLabel.setText(f"Page {currentItemPage + 1} of {total_pages}")
    itemPrev.setEnabled(currentItemPage > 0)
    itemNext.setEnabled(currentItemPage < total_pages - 1)

# def load_persons(personTable, personNext, personPrev, personPageLabel, currentPersonPage):
#     persons = dbfunctions.get_all_persons()

#     table = personTable # pa change to persons table widget pls
#     table.setRowCount(0)
#     table.setColumnCount(6)
#     table.setHorizontalHeaderLabels([
#         "Person ID", "First Name", "Last Name", "Phone Number", "Department", "Proof ID"
#     ])

#     for row_num, person in enumerate(persons):
#         table.insertRow(row_num)
#         for col, value in enumerate(person):
#             table.setItem(row_num, col, QtWidgets.QTableWidgetItem(str(value)))

def load_match_table(matchTable, itemNextButton, itemPrevButton, personPageLabel_2, currentItemPage, ROWS_PER_PAGE, matches):
    matchTable.setRowCount(0)
    matchTable.setColumnCount(6)
    matchTable.setHorizontalHeaderLabels([
        "Item ID", "Name", "Category", "Date Lost", "Location", "Reported By"
    ])

    total_records = len(matches)
    total_pages = max(1, (total_records + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE)
    start = currentItemPage * ROWS_PER_PAGE
    end = start + ROWS_PER_PAGE
    page_matches = matches[start:end]

    for row, item in enumerate(page_matches):
        matchTable.insertRow(row)
        matchTable.setItem(row, 0, QTableWidgetItem(str(item.get("ItemID", ""))))
        matchTable.setItem(row, 1, QTableWidgetItem(str(item.get("Name", ""))))
        matchTable.setItem(row, 2, QTableWidgetItem(str(item.get("Category", ""))))
        # Convert DateLost to string if it's a datetime object
        date_lost = item.get("DateLost", "")
        if hasattr(date_lost, "strftime"):
            date_lost = date_lost.strftime("%Y-%m-%d %H:%M:%S")
        matchTable.setItem(row, 3, QTableWidgetItem(str(date_lost)))
        matchTable.setItem(row, 4, QTableWidgetItem(str(item.get("LocationLost", ""))))
        matchTable.setItem(row, 5, QTableWidgetItem(str(item.get("ReportedBy", ""))))

    personPageLabel_2.setText(f"Page {currentItemPage + 1} of {total_pages}")
    itemPrevButton.setEnabled(currentItemPage > 0)
    itemNextButton.setEnabled(currentItemPage < total_pages - 1)

def display_image_in_cell(table, row, image_path):
    label = ClickableLabel(image_path)
    label.setAlignment(Qt.AlignCenter)

    if image_path and os.path.exists(image_path):
        pixmap = QPixmap(image_path).scaled(
            64, 64,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        label.setPixmap(pixmap)
    else:
        label.setText("No Image")

    table.setCellWidget(row, 0, label)