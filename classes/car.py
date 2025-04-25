class Car:
    def __init__(self, car_id, type, make, model, name, price):
        self.id = car_id
        self.type = type
        self.make = make
        self.model = model
        self.name = name
        self.price = price

    def __repr__(self):
        return (
            f"Car(id={self.id}, type='{self.type}', make='{self.make}', "
            f"model='{self.model}', name='{self.name}', price={self.price})"
        )
