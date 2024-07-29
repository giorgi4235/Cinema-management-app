from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from database import add_customer, update_customer

class CustomerEntryDialog(QDialog):
    def __init__(self, parent=None, customer=None):
        super().__init__(parent)
        self.customer = customer
        self.setWindowTitle("Add Customer" if customer is None else "Edit Customer")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()

        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_edit)
        layout.addWidget(QLabel("Phone:"))
        layout.addWidget(self.phone_edit)

        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_customer)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        if self.customer:
            self.name_edit.setText(self.customer[1])
            self.email_edit.setText(self.customer[2])
            self.phone_edit.setText(self.customer[3])

    def save_customer(self):
        name = self.name_edit.text().strip()
        email = self.email_edit.text().strip()
        phone = self.phone_edit.text().strip()

        if not all([name, email]):
            QMessageBox.warning(self, "Incomplete Data", "Name and Email are required fields.")
            return

        try:
            if self.customer:
                update_customer(self.customer[0], name, email, phone)
            else:
                add_customer(name, email, phone)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")