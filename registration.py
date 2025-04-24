import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from reservation import ReservationWindow


class RegistrationWindow(QDialog):
    def __init__(self):
        super(RegistrationWindow, self).__init__()
        loadUi("registration.ui", self)

        self.Book = self.findChild(QtWidgets.QPushButton, "Book")
        self.Book.clicked.connect(self.open_reservation_window)


    def open_reservation_window(self):
        self.reservation_dialog = ReservationWindow()
        self.reservation_dialog.exec_()

