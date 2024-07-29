from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QScrollArea, QTableWidgetItem, QApplication
from PySide6.QtCore import Qt, QFile
from ui_app import Ui_MainWindow
from movie_entry import MovieEntryDialog
from customer_entry import CustomerEntryDialog
from database import get_all_movies, get_all_customers

class MainScreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.setWindowTitle("ჩინემა მენეგმენტ")

        #window size
        self.setMinimumSize(865, 587)
        self.setMaximumSize(865, 587)

        # hide icon menu
        self.icon_text_menu.setHidden(True)

        # connect button
        self.movies1_btn.clicked.connect(self.switch_to_movie)
        self.movies2_btn.clicked.connect(self.switch_to_movie)

        self.customers1_btn.clicked.connect(self.switch_to_customer)
        self.customers2_btn.clicked.connect(self.switch_to_customer)
        self.add_movie_button.clicked.connect(self.open_movie_entry)
        self.add_customer_button.clicked.connect(self.open_customer_entry)

        self.search_line_edit.textChanged.connect(self.search)


        self.load_movies()
        self.load_customers()
    #switch to different page
    def switch_to_movie(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_customer(self):
        self.stackedWidget.setCurrentIndex(1)

    def load_movies(self):
        movies = get_all_movies()
        self.tableWidget.setRowCount(len(movies))
        for row, movie in enumerate(movies):
            for col, value in enumerate(movie):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))
        self.tableWidget.resizeColumnsToContents()

    def load_customers(self):
        customers = get_all_customers()
        self.tableWidget_2.setRowCount(len(customers))
        for row, customer in enumerate(customers):
            for col, value in enumerate(customer):
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(value)))
        self.tableWidget_2.resizeColumnsToContents()

    def search_movies(self, text):
        for row in range(self.tableWidget.rowCount()):
            match = False
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.tableWidget.setRowHidden(row, not match)

    def search_customers(self, text):
        for row in range(self.tableWidget_2.rowCount()):
            match = False
            for col in range(self.tableWidget_2.columnCount()):
                item = self.tableWidget_2.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.tableWidget_2.setRowHidden(row, not match)

    def search(self, text):
        if self.stackedWidget.currentIndex() == 0:
            self.search_movies(text)
        else:
            self.search_customers(text)

    def open_movie_entry(self):
        dialog = MovieEntryDialog()
        if dialog.exec():
            self.load_movies()

    def open_customer_entry(self):
        dialog = CustomerEntryDialog()
        if dialog.exec():
            self.load_customers()


    def setup_connections(self):
        pass
