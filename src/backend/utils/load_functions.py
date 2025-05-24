from PyQt5 import QtWidgets
from src.backend.database import dbfunctions

def load_reported_items(table_widget):
    all_items = dbfunctions.get_all_items()
    reported_items = [item for item in all_items if item[4] == "Reported"]

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

def load_surrendered_items(table_widget):
    all_items = dbfunctions.get_all_items()
    surrendered_items = [item for item in all_items if item[4] == "Surrendered"]

    table = surrendered_table # pa change to surrendered table widget pls
    table.setRowCount(0)
    table.setColumnCount(8)
    table.setHorizontalHeaderLabels([
        "Item ID", "Category", "Name", "Description", "Status", "Location", "Date", "Surrendered By"
    ])

    for row_num, item in enumerate(surrendered_items):
        table.insertRow(row_num)
        for col, value in enumerate(item):
            table.setItem(row_num, col, QtWidgets.QTableWidgetItem(str(value)))

def load_claimed_items(table_widget):
    all_items = dbfunctions.get_all_items()
    claimed_items = [item for item in all_items if item[4] == "Claimed"]

    table = table_widget # pa change to claimed table widget pls
    table.setRowCount(0)
    table.setColumnCount(8)
    table.setHorizontalHeaderLabels([
        "Item ID", "Category", "Name", "Description", "Status", "Location", "Date", "Claimed By"
    ])

    for row_num, item in enumerate(claimed_items):
        table.insertRow(row_num)
        for col, value in enumerate(item):
            table.setItem(row_num, col, QtWidgets.QTableWidgetItem(str(value)))

def load_persons(personTable):
    persons = dbfunctions.get_all_persons()

    table = personTable # pa change to persons table widget pls
    table.setRowCount(0)
    table.setColumnCount(6)
    table.setHorizontalHeaderLabels([
        "Person ID", "First Name", "Last Name", "Phone Number", "Department", "Proof ID"
    ])

    for row_num, person in enumerate(persons):
        table.insertRow(row_num)
        for col, value in enumerate(person):
            table.setItem(row_num, col, QtWidgets.QTableWidgetItem(str(value)))