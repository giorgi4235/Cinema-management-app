from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(865, 587)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 12, 851, 573))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.icon_menu = QWidget(self.layoutWidget)
        self.icon_menu.setObjectName(u"icon_menu")
        self.icon_menu.setMinimumSize(QSize(81, 571))
        self.icon_menu.setMaximumSize(QSize(81, 571))
        self.icon_menu.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.layoutWidget1 = QWidget(self.icon_menu)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 61, 541))
        self.sidemenu = QVBoxLayout(self.layoutWidget1)
        self.sidemenu.setSpacing(15)
        self.sidemenu.setObjectName(u"sidemenu")
        self.sidemenu.setContentsMargins(10, 20, 10, 10)
        self.logo1_label = QLabel(self.layoutWidget1)
        self.logo1_label.setObjectName(u"logo1_label")
        self.logo1_label.setMinimumSize(QSize(41, 41))
        self.logo1_label.setMaximumSize(QSize(41, 41))
        self.logo1_label.setPixmap(QPixmap(u":/icons/icons/logo2.png"))
        self.logo1_label.setScaledContents(True)

        self.sidemenu.addWidget(self.logo1_label)

        self.movies1_btn = QPushButton(self.layoutWidget1)
        self.movies1_btn.setObjectName(u"movies1_btn")
        self.movies1_btn.setMinimumSize(QSize(41, 41))
        self.movies1_btn.setMaximumSize(QSize(41, 41))
        self.movies1_btn.setStyleSheet(u"QPushButton{\n"
"	padding-left: - 60px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/movie.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.movies1_btn.setIcon(icon)
        self.movies1_btn.setIconSize(QSize(31, 31))
        self.movies1_btn.setCheckable(True)
        self.movies1_btn.setChecked(False)
        self.movies1_btn.setAutoExclusive(True)

        self.sidemenu.addWidget(self.movies1_btn)

        self.customers1_btn = QPushButton(self.layoutWidget1)
        self.customers1_btn.setObjectName(u"customers1_btn")
        self.customers1_btn.setMinimumSize(QSize(41, 41))
        self.customers1_btn.setMaximumSize(QSize(41, 41))
        self.customers1_btn.setStyleSheet(u"QPushButton{\n"
"	padding-left: - 60px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/customer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.customers1_btn.setIcon(icon1)
        self.customers1_btn.setIconSize(QSize(31, 31))
        self.customers1_btn.setCheckable(True)
        self.customers1_btn.setAutoExclusive(True)

        self.sidemenu.addWidget(self.customers1_btn)

        self.verticalSpacer = QSpacerItem(20, 278, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidemenu.addItem(self.verticalSpacer)

        self.exit1_btn = QPushButton(self.layoutWidget1)
        self.exit1_btn.setObjectName(u"exit1_btn")
        self.exit1_btn.setMinimumSize(QSize(41, 41))
        self.exit1_btn.setMaximumSize(QSize(41, 41))
        self.exit1_btn.setStyleSheet(u"QPushButton{\n"
"	padding-left: - 60px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit1_btn.setIcon(icon2)
        self.exit1_btn.setIconSize(QSize(31, 31))
        self.exit1_btn.setCheckable(True)
        self.exit1_btn.setAutoExclusive(True)

        self.sidemenu.addWidget(self.exit1_btn)


        self.horizontalLayout_5.addWidget(self.icon_menu)

        self.icon_text_menu = QWidget(self.layoutWidget)
        self.icon_text_menu.setObjectName(u"icon_text_menu")
        self.icon_text_menu.setMinimumSize(QSize(190, 570))
        self.icon_text_menu.setMaximumSize(QSize(190, 570))
        self.icon_text_menu.setStyleSheet(u"QWidget{\n"
"background-color: rgb(0, 0, 0);\n"
"}")
        self.layoutWidget2 = QWidget(self.icon_text_menu)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(9, 10, 171, 541))
        self.sidemenu_text = QVBoxLayout(self.layoutWidget2)
        self.sidemenu_text.setSpacing(20)
        self.sidemenu_text.setObjectName(u"sidemenu_text")
        self.sidemenu_text.setContentsMargins(5, 20, 0, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.logo2_label = QLabel(self.layoutWidget2)
        self.logo2_label.setObjectName(u"logo2_label")
        self.logo2_label.setMinimumSize(QSize(41, 41))
        self.logo2_label.setMaximumSize(QSize(41, 41))
        self.logo2_label.setPixmap(QPixmap(u":/icons/icons/logo2.png"))
        self.logo2_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo2_label)

        self.logo2_text_label = QLabel(self.layoutWidget2)
        self.logo2_text_label.setObjectName(u"logo2_text_label")
        self.logo2_text_label.setMinimumSize(QSize(80, 41))
        self.logo2_text_label.setMaximumSize(QSize(80, 41))
        font = QFont()
        font.setFamilies([u"Segoe Fluent Icons"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.logo2_text_label.setFont(font)
        self.logo2_text_label.setStyleSheet(u"color: rgb(107, 255, 186);\n"
"")

        self.horizontalLayout.addWidget(self.logo2_text_label)


        self.sidemenu_text.addLayout(self.horizontalLayout)

        self.movies2_btn = QPushButton(self.layoutWidget2)
        self.movies2_btn.setObjectName(u"movies2_btn")
        self.movies2_btn.setMinimumSize(QSize(120, 31))
        self.movies2_btn.setMaximumSize(QSize(120, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.movies2_btn.setFont(font1)
        self.movies2_btn.setStyleSheet(u"QPushButton{\n"
"color: rgb(107, 255, 186);\n"
"padding-left:-30px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.movies2_btn.setIcon(icon)
        self.movies2_btn.setIconSize(QSize(22, 22))
        self.movies2_btn.setCheckable(True)
        self.movies2_btn.setAutoExclusive(True)

        self.sidemenu_text.addWidget(self.movies2_btn)

        self.customers2_btn = QPushButton(self.layoutWidget2)
        self.customers2_btn.setObjectName(u"customers2_btn")
        self.customers2_btn.setMinimumSize(QSize(120, 31))
        self.customers2_btn.setMaximumSize(QSize(120, 31))
        self.customers2_btn.setFont(font1)
        self.customers2_btn.setStyleSheet(u"QPushButton{\n"
"color: rgb(107, 255, 186);\n"
"padding-left: - 60px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"}")
        self.customers2_btn.setIcon(icon1)
        self.customers2_btn.setIconSize(QSize(22, 22))
        self.customers2_btn.setCheckable(True)
        self.customers2_btn.setChecked(False)
        self.customers2_btn.setAutoExclusive(True)

        self.sidemenu_text.addWidget(self.customers2_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 268, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidemenu_text.addItem(self.verticalSpacer_2)

        self.exit2_btn = QPushButton(self.layoutWidget2)
        self.exit2_btn.setObjectName(u"exit2_btn")
        self.exit2_btn.setMinimumSize(QSize(120, 41))
        self.exit2_btn.setMaximumSize(QSize(120, 41))
        font2 = QFont()
        font2.setPointSize(18)
        self.exit2_btn.setFont(font2)
        self.exit2_btn.setStyleSheet(u"QPushButton{\n"
"color: rgb(107, 255, 186);\n"
"padding-left: - 60px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"}")
        self.exit2_btn.setIcon(icon2)
        self.exit2_btn.setIconSize(QSize(31, 31))
        self.exit2_btn.setCheckable(True)
        self.exit2_btn.setAutoExclusive(True)

        self.sidemenu_text.addWidget(self.exit2_btn)


        self.horizontalLayout_5.addWidget(self.icon_text_menu)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, -1, -1, -1)
        self.menu_btn = QPushButton(self.header_widget)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setMinimumSize(QSize(51, 41))
        self.menu_btn.setMaximumSize(QSize(51, 41))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_btn.setIcon(icon3)
        self.menu_btn.setIconSize(QSize(35, 31))
        self.menu_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.menu_btn)

        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(110, 41))
        self.label.setMaximumSize(QSize(110, 41))
        self.label.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.search_line_edit = QLineEdit(self.header_widget)
        self.search_line_edit.setObjectName(u"search_line_edit")
        self.search_line_edit.setMinimumSize(QSize(250, 25))
        self.search_line_edit.setMaximumSize(QSize(250, 25))
        font3 = QFont()
        font3.setPointSize(8)
        self.search_line_edit.setFont(font3)
        self.search_line_edit.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px;\n"
"}")
        self.search_line_edit.setCursorPosition(9)

        self.horizontalLayout_3.addWidget(self.search_line_edit)

        self.label_2 = QLabel(self.header_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(41, 41))
        self.label_2.setMaximumSize(QSize(41, 41))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/search.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.header_widget)

        self.table_window = QWidget(self.layoutWidget)
        self.table_window.setObjectName(u"table_window")
        self.table_window.setMinimumSize(QSize(551, 501))
        self.table_window.setMaximumSize(QSize(551, 501))
        self.table_window.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.table_window)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, 9, 551, 481))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.widget = QWidget(self.page_1)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 561, 491))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Movies_label = QLabel(self.widget)
        self.Movies_label.setObjectName(u"Movies_label")
        self.Movies_label.setMinimumSize(QSize(120, 51))
        self.Movies_label.setMaximumSize(QSize(120, 51))
        font4 = QFont()
        font4.setFamilies([u"Sans Serif Collection"])
        font4.setPointSize(22)
        font4.setBold(True)
        self.Movies_label.setFont(font4)

        self.verticalLayout_2.addWidget(self.Movies_label)

        self.add_movie_button = QPushButton(self.widget)
        self.add_movie_button.setObjectName(u"add_movie_button")

        self.verticalLayout_2.addWidget(self.add_movie_button)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.Customers_label = QLabel(self.page_2)
        self.Customers_label.setObjectName(u"Customers_label")
        self.Customers_label.setGeometry(QRect(190, 130, 201, 171))
        self.layoutWidget_2 = QWidget(self.page_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 0, 561, 491))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Movies_label_2 = QLabel(self.layoutWidget_2)
        self.Movies_label_2.setObjectName(u"Movies_label_2")
        self.Movies_label_2.setMinimumSize(QSize(120, 51))
        self.Movies_label_2.setMaximumSize(QSize(150, 51))
        self.Movies_label_2.setFont(font4)

        self.verticalLayout_5.addWidget(self.Movies_label_2)

        self.add_customer_button = QPushButton(self.layoutWidget_2)
        self.add_customer_button.setObjectName(u"add_movie_button_2")

        self.verticalLayout_5.addWidget(self.add_customer_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.tableWidget_2 = QTableWidget(self.layoutWidget_2)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_4.addWidget(self.tableWidget_2)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.table_window)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.movies2_btn.toggled.connect(self.movies1_btn.setChecked)
        self.customers2_btn.toggled.connect(self.customers1_btn.setChecked)
        self.exit2_btn.toggled.connect(self.exit1_btn.setChecked)
        self.exit1_btn.toggled.connect(MainWindow.close)
        self.menu_btn.toggled.connect(self.icon_text_menu.setVisible)
        self.menu_btn.toggled.connect(self.icon_menu.setHidden)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo1_label.setText("")
        self.movies1_btn.setText("")
        self.customers1_btn.setText("")
        self.exit1_btn.setText("")
        self.logo2_label.setText("")
        self.logo2_text_label.setText(QCoreApplication.translate("MainWindow", u"Cinema", None))
        self.movies2_btn.setText(QCoreApplication.translate("MainWindow", u"Movies", None))
        self.customers2_btn.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.exit2_btn.setText(QCoreApplication.translate("MainWindow", u" exit", None))
        self.menu_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.search_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.label_2.setText("")
        self.Movies_label.setText(QCoreApplication.translate("MainWindow", u"Movies", None))
        self.add_movie_button.setText(QCoreApplication.translate("MainWindow", u"add movie", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Genre", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Release Year", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Show Time", None));
        self.Customers_label.setText(QCoreApplication.translate("MainWindow", u"customers", None))
        self.Movies_label_2.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.add_customer_button.setText(QCoreApplication.translate("MainWindow", u"add customer", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
    # retranslateUi

