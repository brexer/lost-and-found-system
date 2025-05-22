import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from pagination import Ui_MainWindow

class MainClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Pagination state
        self.page = 0
        self.page_size = 10
        self.total_pages = 0

        # Connect button signals
        self.prevButton.clicked.connect(self.previous_page)
        self.nextButton.clicked.connect(self.next_page)

        # Initialize total pages and load first page of data
        self.update_total_pages()
        self.load_data()

    def connectToDatabase(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="admin",
            database="ssis"
        )

    def update_total_pages(self):
        conn = self.connectToDatabase()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM student")
        total_records = cursor.fetchone()[0]
        self.total_pages = (total_records + self.page_size - 1) // self.page_size
        cursor.close()
        conn.close()

    def load_data(self):
        conn = self.connectToDatabase()
        cursor = conn.cursor()
        offset = self.page * self.page_size

        cursor.execute(f"SELECT * FROM student LIMIT {self.page_size} OFFSET {offset}")  # Replace with your actual table name
        data = cursor.fetchall()
        headers = [i[0] for i in cursor.description]

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        self.pageLabel.setText(f"Page {self.page + 1} of {self.total_pages}")
        self.prevButton.setEnabled(self.page > 0)
        self.nextButton.setEnabled(self.page < self.total_pages - 1)

        cursor.close()
        conn.close()

    def next_page(self):
        if self.page < self.total_pages - 1:
            self.page += 1
            self.load_data()

    def previous_page(self):
        if self.page > 0:
            self.page -= 1
            self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec())
