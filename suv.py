import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from reservation import ReservationWindow
from registration import RegistrationWindow


class SuvWindow(QDialog):
    def __init__(self):
        super(SuvWindow, self).__init__()
        loadUi("suv.ui", self)

        self.Book = self.findChild(QtWidgets.QPushButton, "Book")
        self.Book.clicked.connect(self.open_registration_window)
        self.Book2 = self.findChild(QtWidgets.QPushButton, "Book2")
        self.Book2.clicked.connect(self.open_registration_window)
        self.Book3 = self.findChild(QtWidgets.QPushButton, "Book3")
        self.Book3.clicked.connect(self.open_registration_window)
        self.Book4 = self.findChild(QtWidgets.QPushButton, "Book4")
        self.Book4.clicked.connect(self.open_registration_window)

    def open_reservation_window(self):
        self.reservation_dialog = ReservationWindow()
        self.reservation_dialog.exec_()

    def open_registration_window(self):
        self.registration_dialog = RegistrationWindow()
        self.registration_dialog.exec_()