class Rental:
    def __init__(self, rental_id, user_id, car_id, start_date, end_date, returned):
        self.rental_id = rental_id
        self.user_id = user_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.returned = returned

    def __repr__(self):
        return (f"Rental(rental_id={self.rental_id}, user_id={self.user_id}, car_id={self.car_id}, "
                f"start_date='{self.start_date}', end_date='{self.end_date}', returned={self.returned})")
