from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTimeEdit, QMessageBox
from PyQt6.QtCore import QTime
from database import add_movie

class MovieEntryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Movie")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.name_edit = QLineEdit()
        self.genre_edit = QLineEdit()
        self.year_edit = QLineEdit()
        self.time_edit = QTimeEdit()

        layout.addWidget(QLabel("Movie Name:"))
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("Genre:"))
        layout.addWidget(self.genre_edit)
        layout.addWidget(QLabel("Release Year:"))
        layout.addWidget(self.year_edit)
        layout.addWidget(QLabel("Show Time:"))
        layout.addWidget(self.time_edit)

        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_movie)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def save_movie(self):
        name = self.name_edit.text().strip()
        genre = self.genre_edit.text().strip()
        year_text = self.year_edit.text().strip()
        show_time = self.time_edit.time().toString("HH:mm")

        if not all([name, genre, year_text, show_time]):
            QMessageBox.warning(self, "Incomplete Data", "Please fill in all fields.")
            return

        try:
            year = int(year_text)
            if year <= 0:
                raise ValueError("Year must be a positive integer.")
        except ValueError:
            QMessageBox.warning(self, "Invalid Year", "Please enter a valid year (positive integer).")
            return

        add_movie(name, genre, year, show_time)
        self.accept()