from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class CreateaccWindow(QDialog):
    def __init__(self):
        super(CreateaccWindow, self).__init__()
        loadUi("createacc.ui", self)
