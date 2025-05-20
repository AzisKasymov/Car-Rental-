class Car:
    def __init__(self, model, car_class ,price_per_day, amount):
        self.__model = model
        self.__car_class = car_class
        self.__price_per_day = price_per_day
        self.__amount = amount

    def get_model(self):
        return self.__model
    def get_car_class(self):
        return self.__car_class
    def get_price_per_day(self):
        return self.__price_per_day
    def get_amount(self):
        return self.__amount

    def set_model(self, model):
        self.__model = model
    def set_car_class(self, car_class):
        self.__car_class = car_class
    def set_price_per_day(self, price_per_day):
        self.__price_per_day = price_per_day
    def set_amount(self, amount):
        self.__amount = amount

