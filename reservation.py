from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class ReservationWindow(QDialog):
    def __init__(self):
        super(ReservationWindow, self).__init__()
        loadUi("reservation.ui", self)
