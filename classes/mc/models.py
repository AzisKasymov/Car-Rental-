from classes.dao.carDAO import CarDAO
from classes.dao.userDAO import UserDAO
from classes.dao.rentalDAO import RentalDAO

class Model:
    def __init__(self, db_file='cars.db'):
        self.car_dao = CarDAO(db_file)
        self.user_dao = UserDAO(db_file)
        self.rental_dao = RentalDAO(db_file)

    def add_user(self, name, email, password, is_admin=False):
        return self.user_dao.add_user(name, email, password, is_admin)

    def get_user(self, user_id):
        return self.user_dao.get_user_by_id(user_id)

    def list_users(self):
        return self.user_dao.get_all_users()

    def authenticate_user(self, email, password):
        user = self.user_dao.get_user_by_email(email)
        return user if user and user.password == password else None

    def add_car(self, type_, model, name, price):
        return self.car_dao.add_car(type_, model, name, price)

    def list_cars(self):
        return self.car_dao.get_all_cars()

    def get_car(self, car_id):
        return self.car_dao.get_car_by_id(car_id)

    def search_cars(self, term):
        return [c for c in self.list_cars() if term.lower() in c.name.lower()]

    def update_car(self, car_id, type_=None, model=None, name=None, price=None):
        fields = {}
        if type_ is not None: fields['type'] = type_
        if model is not None: fields['model'] = model
        if name is not None: fields['name'] = name
        if price is not None: fields['price'] = price
        if fields:
            self.car_dao.update_car(car_id, **fields)
        return car_id

    def delete_car(self, car_id):
        self.car_dao.delete_car_by_id(car_id)
        return car_id

    def book_rental(self, user_id, car_id, start_date, end_date):
        return self.rental_dao.add_rental(user_id, car_id, start_date, end_date)

    def list_rentals(self):
        return self.rental_dao.get_all_rentals()
