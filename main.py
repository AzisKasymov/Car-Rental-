import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from sedan import SedanWindow
from crossover import CrossoverWindow
from suv import SuvWindow
from login import Login
from reservation import ReservationWindow

class MainWindow(QMainWindow):
    def __init__(self,):
        super(MainWindow, self).__init__()
        loadUi("MainWindow.ui", self)

        self.Sedan = self.findChild(QtWidgets.QPushButton, "Sedan")
        self.Sedan.clicked.connect(self.open_sedan_window)
        self.Crossover = self.findChild(QtWidgets.QPushButton, "Crossover")
        self.Crossover.clicked.connect(self.open_crossover_window)
        self.SUV = self.findChild(QtWidgets.QPushButton, "SUV")
        self.SUV.clicked.connect(self.open_suv_window)
        self.Login = self.findChild(QtWidgets.QPushButton, "Login")
        self.Login.clicked.connect(self.open_login_window)
        self.Book = self.findChild(QtWidgets.QPushButton, "Book")
        self.Book.clicked.connect(self.open_reservation_window)

    def open_sedan_window(self):
        self.sedan_dialog = SedanWindow()
        self.sedan_dialog.exec_()

    def open_crossover_window(self):
        self.crossover_dialog = CrossoverWindow()
        self.crossover_dialog.exec_()

    def open_suv_window(self):
        self.suv_dialog = SuvWindow()
        self.suv_dialog.exec_()

    def open_login_window(self):
        login_dialog = Login()
        if login_dialog.exec_() == QDialog.Accepted:
            user_email = login_dialog.logged_email
            self.welcomeLabel.setText(f"Hello, {user_email}!")

    def open_reservation_window(self):
        self.reservation_dialog = ReservationWindow()
        self.reservation_dialog.exec_()




app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())



