import re
from classes.user import User
from dao.user_dao import UserDAO
from dao.history_dao import HistoryDAO
from classes.history import History
from dao.car_dao import CarDAO
from classes.car import Car
from PyQt6 import QtCore

class Model:
    def __init__(self):
        self.dao = UserDAO("/Users/argenkulzhanov/Desktop/Designer/baisal/rent_cars.sqlite")
        self.history_dao = HistoryDAO("/Users/argenkulzhanov/Desktop/Designer/baisal/rent_cars.sqlite")
        self.car_dao = CarDAO("/Users/argenkulzhanov/Desktop/Designer/baisal/rent_cars.sqlite")


    def is_strong_password(self, password):
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in password):
            return False
        return True

    def is_valid_email(self, email):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", email)

    def is_valid_username(self, username):
        return re.match(r"^[A-Za-z0-9_]+$", username)

    def create_account(self, username, password):
        if not self.is_valid_username(username):
            return False, "Username must contain only English letters and digits."

        if not self.is_strong_password(password):
            return False, "Password must be at least 8 characters and include uppercase, lowercase, number, and symbol."

        if self.dao.find_by_username(username):
            return False, "This username already exists."



        user = User(username, password)
        self.dao.insert(user)
        return True, "Your account has been created successfully."

    def validate_login(self, username, password):
        if not username or not password:
            return False, "Please fill in both fields."

        user = self.dao.find_by_username(username)
        if not user:
            return False, "User not found."

        if user.get_password() != password:
            return False, "Incorrect password."

        return True, "Login successful."



    def book_car(self, username, car, pick_up_address, return_address, pick_up_date, return_date):
        # Validate input fields
        if car == "List of cars" or pick_up_address == "Pick-up Address" or return_address == "Return address":
            raise ValueError("Please select all required fields.")

        if pick_up_date < QtCore.QDateTime.currentDateTime():
            raise ValueError("Pickup date cannot be earlier than today.")

        if return_date <= pick_up_date:
            raise ValueError("Return date must be later than pickup date.")

        # Get the price of the car
        total_price = self.car_dao.get_price_by_model(car)
        if total_price is None:
            raise ValueError("Car model not found in the database.")

        # Save booking to history
        pick_up_date_to_string = pick_up_date.toString("yyyy-MM-dd HH:mm:ss")
        return_date_to_string = return_date.toString("yyyy-MM-dd HH:mm:ss")
        history = History(username, car, pick_up_address, return_address, pick_up_date_to_string,return_date_to_string, total_price)
        self.history_dao.insert(history)

        return total_price