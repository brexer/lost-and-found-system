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

