from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from src.backend.database import dbfunctions
from src.backend.utils import match_checker as match

def load_reported_items(reportTable, reportNext, reportPrev, reportPageLabel, currentReportPage, page_size, search_text=""):
    reported_items, total_records = dbfunctions.get_all_reported_items(currentReportPage, page_size, search_text)
    total_pages = max(1, (total_records + page_size - 1) // page_size)

    table = reportTable
    table.setRowCount(0)
    table.setColumnCount(8)
    table.setHorizontalHeaderLabels([
        "Item ID", "Category", "Name", "Description", "Status", "Location", "Date", "Reported By"
    ])
    
    for row_num, item in enumerate(reported_items):
        table.insertRow(row_num)
        for col, value in enumerate(item):
            table.setItem(row_num, col, QtWidgets.QTableWidgetItem(str(value)))

    reportPageLabel.setText(f"Page {currentReportPage + 1} of {total_pages}")
    reportPrev.setEnabled(currentReportPage > 0)
    reportNext.setEnabled(currentReportPage < total_pages - 1)

def load_surrendered_items(surrenderTable, surrenderNext, surrenderPrev, surrenderPageLabel, currentSurrenderPage, page_size, search_text=""):
    surrendered_items, total_records = dbfunctions.get_all_surrendered_items(currentSurrenderPage, page_size, search_text)
    total_pages = max(1, (total_records + page_size - 1) // page_size)

    table = surrenderTable
    table.setRowCount(0)
    table.setColumnCount(8)
    table.setHorizontalHeaderLabels([
        "Item ID", "Category", "Name", "Description", "Status", "Location", "Date", "Surrendered By"
    ])

    for row_num, item in enumerate(surrendered_items):
        table.insertRow(row_num)
        for col, value in enumerate(item):
            table.setItem(row_num, col, QtWidgets.QTableWidgetItem(str(value)))

    surrenderPageLabel.setText(f"Page {currentSurrenderPage + 1} of {total_pages}")
    surrenderPrev.setEnabled(currentSurrenderPage > 0)
    surrenderNext.setEnabled(currentSurrenderPage < total_pages - 1)

def load_claimed_items(claimTable, claimNext, claimPrev, claimPageLabel, currentClaimPage, page_size):
    claimed_items, total_records = dbfunctions.get_all_claimed_items(currentClaimPage, page_size)
    total_pages = max(1, (total_records + page_size - 1) // page_size)
    # all_items = dbfunctions.get_all_items()
    # claimed_items = [item for item in all_items if item[4] == "Claimed"]

    table = claimTable
    table.setRowCount(0)
    table.setColumnCount(8)
    table.setHorizontalHeaderLabels([
        "Item ID", "Category", "Name", "Description", "Status", "Location", "Date", "Claimed By"
    ])

    for row_num, item in enumerate(claimed_items):
        table.insertRow(row_num)
        for col, value in enumerate(item):
            table.setItem(row_num, col, QtWidgets.QTableWidgetItem(str(value)))

    claimPageLabel.setText(f"Page {currentClaimPage + 1} of {total_pages}")
    claimPrev.setEnabled(currentClaimPage > 0)
    claimNext.setEnabled(currentClaimPage < total_pages - 1)

def load_persons(personTable, personNext, personPrev, personPageLabel, currentPersonPage, page_size, search_text=""):
    persons, total_records = dbfunctions.get_all_persons(currentPersonPage, page_size, search_text)
    total_pages = max(1, (total_records + page_size - 1) // page_size)

    table = personTable
    table.setRowCount(0)
    table.setColumnCount(6)
    table.setHorizontalHeaderLabels([
        "Person ID", "First Name", "Last Name", "Phone Number", "Department", "Proof ID"
    ])

    for row_num, person in enumerate(persons):
        table.insertRow(row_num)
        for col, value in enumerate(person):
            table.setItem(row_num, col, QtWidgets.QTableWidgetItem(str(value)))

    personPageLabel.setText(f"Page {currentPersonPage + 1} of {total_pages}")
    personPrev.setEnabled(currentPersonPage > 0)
    personNext.setEnabled(currentPersonPage < total_pages - 1)

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

def load_match_table(matchTable, matchNext, matchPrev, matchPageLabel, currentMatchPage, page_size, matches):
    total_records = len(matches)
    total_pages = max(1, (total_records + page_size - 1) // page_size)

    # Calculate start and end indices for the current page
    start = currentMatchPage * page_size
    end = start + page_size
    page_matches = matches[start:end]

    matchTable.setRowCount(0)
    matchTable.setColumnCount(6)
    matchTable.setHorizontalHeaderLabels([
        "Item ID", "Name", "Category", "Date Lost", "Location", "Reported By"
    ])

    for row, item in enumerate(page_matches):
        matchTable.insertRow(row)
        matchTable.setItem(row, 0, QTableWidgetItem(str(item.get("ItemID", ""))))
        matchTable.setItem(row, 1, QTableWidgetItem(item.get("Name", "")))
        matchTable.setItem(row, 2, QTableWidgetItem(item.get("Category", "")))
        matchTable.setItem(row, 3, QTableWidgetItem(item.get("DateLost", "")))
        matchTable.setItem(row, 4, QTableWidgetItem(item.get("LocationLost", "")))
        matchTable.setItem(row, 5, QTableWidgetItem(item.get("ReportedBy", "")))

    matchPageLabel.setText(f"Page {currentMatchPage + 1} of {total_pages}")
    matchPrev.setEnabled(currentMatchPage > 0)
    matchNext.setEnabled(currentMatchPage < total_pages - 1)