from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
import pyrebase
from PyQt5.QtWidgets import QMessageBox

firebaseConfig = {
    'apiKey': "AIzaSyAmIS_PsOtZRZ0aKk8BOnBnV38QaATb6E8",
    'authDomain': "authdemo-194eb.firebaseapp.com",
    'databaseURL': "https://authdemo-194eb-default-rtdb.firebaseio.com",
    'projectId': "authdemo-194eb",
    'storageBucket': "authdemo-194eb.appspot.com",
    'messagingSenderId': "850844282331",
    'appId': "1:850844282331:web:7c4be420fff9521053cbfe",
    'measurementId': "G-FJ0HJ06SQ9"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()



class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.logged_email = None

        self.loginbutton.clicked.connect(self.loginfunction)
        self.createaccbutton.clicked.connect(self.gotocreate)

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.invalid.setVisible(False)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        try:
            auth.sign_in_with_email_and_password(email, password)
            self.logged_email = email
            QMessageBox.information(self, "Entrance", "You have logged in successfully.")
            self.accept()
        except:
            self.invalid.setVisible(True)

    def gotocreate(self):
        self.create_dialog = CreateAcc()
        self.create_dialog.exec_()

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("createacc.ui", self)

        self.signupbutton.clicked.connect(self.createaccfunction)

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.invalid.setVisible(False)

    def createaccfunction(self):
        email = self.email.text()
        password = self.password.text()
        confirm = self.confirmpass.text()

        if password == confirm:
            try:
                auth.create_user_with_email_and_password(email, password)
                QMessageBox.information(self, "Success", "Account successfully created! You can now log in.")

                self.accept()

                login_dialog = Login()
                login_dialog.exec_()
            except:
                self.invalid.setText("Error creating account")
                self.invalid.setVisible(True)
        else:
            self.invalid.setText("The passwords do not match")
            self.invalid.setVisible(True)
