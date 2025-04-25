from classes.dao.userDAO import UserDAO
from classes.dao.carDAO import CarDAO
from classes.dao.rentalDAO import RentalDAO

class Controller:
    def __init__(self, db_file='cars.db'):
        self.user_dao = UserDAO(db_file)
        self.car_dao = CarDAO(db_file)
        self.rental_dao = RentalDAO(db_file)

    def handle_add_user(self, name, email, password, is_admin=False):
        return self.user_dao.add_user(name, email, password, is_admin)

    def handle_user_login(self, email, password):
        user = self.user_dao.get_user_by_email(email)
        if user and user.password == password:
            return user
        return None

    def add_car(self, type_, model, name, price):
        return self.car_dao.add_car(type_, model, name, price)

    def list_cars(self):
        return self.car_dao.get_all_cars()

    def get_car(self, car_id):
        return self.car_dao.get_car_by_id(car_id)

    def search_cars(self, term):
        return [c for c in self.list_cars() if term.lower() in c.name.lower()]

    def update_car(self, car_id, **fields):
        return self.car_dao.update_car(car_id, **fields)

    def delete_car(self, car_id):
        return self.car_dao.delete_car_by_id(car_id)

    def book_rental(self, user_id, car_id, start_date, end_date):
        return self.rental_dao.add_rental(user_id, car_id, start_date, end_date)


def populate_filters(self):
    # Fetch the available car types and models from the database via controller or DAO
    car_types = self.controller.get_car_types()  # Ensure this method is implemented
    car_models = self.controller.get_car_models()  # Ensure this method is implemented

    # Clear existing combo box values to avoid duplicates
    self.ui.box_type.clear()
    self.ui.box_model.clear()

    # Add a default "All" option for each filter
    self.ui.box_type.addItem("All Types")
    self.ui.box_model.addItem("All Models")

    # Add the fetched values from the database to the combo boxes
    for car_type in car_types:
        self.ui.box_type.addItem(car_type)
    for car_model in car_models:
        self.ui.box_model.addItem(car_model)
