class History:
    def __init__(self, username,car_model, pickup_address, return_address, start_datetime, end_datetime,total_price):
        self.__username = username
        self.__car_model = car_model
        self.__pickup_address = pickup_address
        self.__return_address = return_address
        self.__start_datetime = start_datetime
        self.__end_datetime = end_datetime
        self.__total_price = total_price

    def get_username(self):
        return self.__username
    def get_car_model(self):
        return self.__car_model
    def get_pickup_address(self):
        return self.__pickup_address
    def get_return_address(self):
        return self.__return_address
    def get_start_datetime(self):
        return self.__start_datetime
    def get_end_datetime(self):
        return self.__end_datetime
    def get_total_price(self):
        return self.__total_price

    def set_username(self, username):
        self.__username = username
    def set_car_model(self, car_model):
        self.__car_model = car_model
    def set_pickup_address(self, pickup_address):
        self.__pickup_address = pickup_address
    def set_return_address(self, return_address):
        self.__return_address = return_address
    def set_start_datetime(self, start_datetime):
        self.__start_datetime = start_datetime
    def set_end_datetime(self, end_datetime):
        self.__end_datetime = end_datetime
    def set_total_price(self, total_price):
        self.__total_price = total_price

