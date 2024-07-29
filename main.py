import sys
from PySide6.QtWidgets import QApplication
from main_screen import MainScreen
from database import create_tables

def main():
    app = QApplication(sys.argv)
    create_tables()
    window = MainScreen()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()