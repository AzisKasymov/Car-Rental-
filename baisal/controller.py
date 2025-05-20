from PyQt6.QtWidgets import QMainWindow, QMessageBox
from pyqt.Mainwindow import Ui_MainWindow
from pyqt.login import Ui_Dialog as Ui_Login
from pyqt.registration import Ui_Dialog as Ui_Registration
from pyqt.suv import Ui_Dialog3 as Ui_suv
from pyqt.crossover import Ui_Dialog as Ui_crossover
from pyqt.sedan import Ui_Dialog1 as Ui_sedan
from pyqt.createacc import Ui_Dialog as Ui_CreateAcc
from model import Model
import requests
from io import BytesIO
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore
from dao.history_dao import HistoryDAO
from dao.car_dao import CarDAO




class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_window = None
        self.login_window = None
        self.registration_window = None
        self.suv_window = None
        self.crossover_window = None
        self.sedan_window = None
        self.createacc_window = None
        self.ui_main = Ui_MainWindow()
        self.ui_login = Ui_Login()
        self.ui_registration = Ui_Registration()
        self.ui_suv = Ui_suv()
        self.ui_crossover = Ui_crossover()
        self.ui_sedan = Ui_sedan()
        self.ui_createacc = Ui_CreateAcc()
        self.current_username = None
        self.model = Model()
        self.car_dao = CarDAO("/Users/argenkulzhanov/Desktop/Designer/baisal/rent_cars.sqlite")
        self.history_dao = HistoryDAO("/Users/argenkulzhanov/Desktop/Designer/baisal/rent_cars.sqlite")
        self.selected_car = None

    def show_main_window(self):
        self.main_window = QMainWindow()
        self.ui_main.setupUi(self.main_window)

        self.main_window.show()
        self.init_main_window_buttons()
        self.load_images()

    def load_images(self):
        self.load_image_from_url(self.ui_main.label_5, "https://cab.kg/img/filter/mob_3.jpg")
        self.load_image_from_url(self.ui_main.label_4, "https://cab.kg/img/filter/mob_2.jpg")
        self.load_image_from_url(self.ui_main.label_2, "https://cab.kg/img/filter/mob_1.jpg")

    def load_images_sedan(self):
        self.load_image_from_url(self.ui_sedan.label_5, "https://cab.kg/img/cars/xgqdMr.jpg")
        self.load_image_from_url(self.ui_sedan.label_4, "https://cab.kg/img/cars/WnbHYB.jpg")
        self.load_image_from_url(self.ui_sedan.label_2, "https://cab.kg/img/cars/b4WR4h.jpg")
        self.load_image_from_url(self.ui_sedan.label_3, "https://cab.kg/img/cars/CkYHaB.jpg")

    def load_images_crossover(self):
        self.load_image_from_url(self.ui_crossover.label_5, "https://cab.kg/img/cars/2Y9hml.jpg")
        self.load_image_from_url(self.ui_crossover.label_4, "https://cab.kg/img/cars/jwFb5v.jpg")
        self.load_image_from_url(self.ui_crossover.label_2, "https://cab.kg/img/cars/KnUq61.jpg")
        self.load_image_from_url(self.ui_crossover.label_3, "https://cab.kg/img/cars/MpIWdk.jpg")

    def load_images_suv(self):
        self.load_image_from_url(self.ui_suv.label_5, "https://cab.kg/img/cars/krkuCq.jpg")
        self.load_image_from_url(self.ui_suv.label_4, "https://cab.kg/img/cars/VUYaHE.jpg")
        self.load_image_from_url(self.ui_suv.label_2, "https://cab.kg/img/cars/MGtVp5.jpg")
        self.load_image_from_url(self.ui_suv.label_3, "https://cab.kg/img/cars/uziUZA.jpg")

    def show_login_window(self):
        self.login_window = QMainWindow()
        self.ui_login.setupUi(self.login_window)
        self.login_window.show()
        self.ui_login.loginbutton.clicked.connect(self.login_account)
        self.ui_login.createaccbutton.clicked.connect(self.show_createacc_window)

    def show_registration_window(self):
        self.registration_window = QMainWindow()
        self.ui_registration.setupUi(self.registration_window)
        self.registration_window.show()
        self.init_registration_window_buttons()

    def show_suv_window(self):
        self.suv_window = QMainWindow()
        self.ui_suv.setupUi(self.suv_window)
        self.suv_window.show()
        self.init_suv_window_buttons()
        self.load_images_suv()

    def show_crossover_window(self):
        self.crossover_window = QMainWindow()
        self.ui_crossover.setupUi(self.crossover_window)
        self.crossover_window.show()
        self.init_crossover_window_buttons()
        self.load_images_crossover()

    def show_sedan_window(self):
        self.sedan_window = QMainWindow()
        self.ui_sedan.setupUi(self.sedan_window)
        self.sedan_window.show()
        self.init_sedan_window_buttons()
        self.load_images_sedan()

    def show_createacc_window(self):
        self.createacc_window = QMainWindow()
        self.ui_createacc.setupUi(self.createacc_window)
        self.createacc_window.show()
        self.ui_createacc.signupbutton.clicked.connect(self.create_account)


    def init_main_window_buttons(self):
        self.ui_main.Book.clicked.connect(self.on_main_book_clicked)
        self.ui_main.Login.clicked.connect(self.show_login_window)
        self.ui_main.Sedan.clicked.connect(self.show_sedan_window)
        self.ui_main.SUV.clicked.connect(self.show_suv_window)
        self.ui_main.Crossover.clicked.connect(self.show_crossover_window)


    def init_registration_window_buttons(self):
        self.ui_registration.Book.clicked.connect(self.sedan_book1)

    def init_suv_window_buttons(self):
        self.ui_suv.Book.clicked.connect(lambda: self.sedan_book1("Toyota Rav4SVU"))
        self.ui_suv.Book2.clicked.connect(lambda: self.sedan_book1("Toyota Fortuner"))
        self.ui_suv.Book3.clicked.connect(lambda: self.sedan_book1("Toyota LandCruisier"))
        self.ui_suv.Book4.clicked.connect(lambda: self.sedan_book1("Lexus LX570"))

    def init_crossover_window_buttons(self):
        self.ui_crossover.Book.clicked.connect(lambda: self.sedan_book1("Hyundai Rav4"))
        self.ui_crossover.Book2.clicked.connect(lambda: self.sedan_book1("Subaru Forester"))
        self.ui_crossover.Book3.clicked.connect(lambda: self.sedan_book1("Kia Seltos"))
        self.ui_crossover.Book4.clicked.connect(lambda: self.sedan_book1("Lexus RX330"))

    def init_sedan_window_buttons(self):
        self.ui_sedan.Book.clicked.connect(lambda: self.sedan_book1("Hyundai Solaris"))
        self.ui_sedan.Book2.clicked.connect(lambda: self.sedan_book1("Chevrolet Cobalt"))
        self.ui_sedan.Book3.clicked.connect(lambda: self.sedan_book1("Toyota Corolla"))
        self.ui_sedan.Book4.clicked.connect(lambda: self.sedan_book1("Hyundai Sonata"))

    def sedan_book1(self, car_name):
        self.selected_car = car_name
        self.show_registration_window()

        try:
            self.ui_registration.Book.clicked.disconnect()
        except TypeError:
            pass

        self.ui_registration.Book.clicked.connect(lambda: self.handle_booking(car_name))

    def handle_booking(self, car_name):
        if self.current_username is None:
            QMessageBox.warning(None, "Error", "Please log in to book a car.")
            return

        pick_up_address = self.ui_registration.comboBox.currentText()
        return_address = self.ui_registration.comboBox_2.currentText()
        pick_up_date = self.ui_registration.dateTimeEdit_2.dateTime()
        return_date = self.ui_registration.dateTimeEdit_3.dateTime()

        if pick_up_address == "Pick-up Address" or return_address == "Return address":
            QMessageBox.warning(None, "Error", "Please select pickup and return addresses.")
            return

        if return_date <= pick_up_date:
            QMessageBox.warning(None, "Error", "Return date must be after pickup date.")
            return

        try:
            total_price = self.model.book_car(
                username=self.current_username,
                car=car_name,
                pick_up_address=pick_up_address,
                return_address=return_address,
                pick_up_date=pick_up_date,
                return_date=return_date
            )

            QMessageBox.information(None, "Booking Successful",
                                    f"Car: {car_name}\n"
                                    f"Pickup: {pick_up_address}\n"
                                    f"Return: {return_address}\n"
                                    f"Pickup Date: {pick_up_date.toString('yyyy-MM-dd HH:mm')}\n"
                                    f"Return Date: {return_date.toString('yyyy-MM-dd HH:mm')}\n"
                                    f"Total Price: {total_price} сом")

            self.car_dao.minus_amount_by_model(car_name)
            self.registration_window.close()

        except ValueError as e:
            QMessageBox.warning(None, "Booking Error", str(e))
        except Exception as e:
            QMessageBox.warning(None, "Unexpected Error", f"An unexpected error occurred:\n{str(e)}")

    def login_account(self):
        self.current_username = self.ui_login.email.text().strip()
        password = self.ui_login.password.text().strip()

        success, message = self.model.validate_login(self.current_username, password)

        if not success:
            QMessageBox.warning(None, "Login Failed", message)
        else:
            QMessageBox.information(None, "Welcome", message)
            self.login_window.close()
            self.ui_main.Login.setText(self.current_username)

    def create_account(self):
        username = self.ui_createacc.email.text().strip()
        password = self.ui_createacc.password.text().strip()
        confirm_password = self.ui_createacc.confirmpass.text().strip()

        success, message = self.model.create_account(username, password)
        if password != confirm_password:
            QMessageBox.warning(None, "Error", "Passwords do not match.")
            return
        if not success:
            QMessageBox.warning(None, "Error", message)
        else:
            QMessageBox.information(None, "Success", message)
            self.show_login_window()
            self.createacc_window.close()

    def load_image_from_url(self, label, url):
        response = requests.get(url)
        if response.status_code == 200:
            image_data = BytesIO(response.content)
            pixmap = QPixmap()
            pixmap.loadFromData(image_data.read())
            label.setPixmap(pixmap)
            label.setScaledContents(True)
        else:
            label.setText("Ошибка загрузки")

    def on_main_book_clicked(self):
        car = self.ui_main.comboBox.currentText()
        pick_up_address = self.ui_main.ksdds.currentText()
        return_address = self.ui_main.comboBox_2.currentText()
        pick_up_date = self.ui_main.dateTimeEdit_2.dateTime()
        return_date = self.ui_main.dateTimeEdit_3.dateTime()

        if self.current_username is None:
            QMessageBox.warning(None, "Error", "Please log in to book a car.")
            return

        try:
            total_price = self.model.book_car(
                username=self.current_username,
                car=car,
                pick_up_address=pick_up_address,
                return_address=return_address,
                pick_up_date=pick_up_date,
                return_date=return_date
            )

            QMessageBox.information(None, "Booking Successful",
                                    f"Car: {car}\nPickup: {pick_up_address}\nReturn: {return_address}\nPickup Date: {pick_up_date.toString()}\nReturn Date: {return_date.toString()}\nTotal Price: {total_price}")
            self.car_dao.minus_amount_by_model(car)
        except ValueError as e:
            QMessageBox.warning(None, "Error", str(e))
        except Exception as e:
            QMessageBox.warning(None, "Error", f"An unexpected error occurred: {str(e)}")
