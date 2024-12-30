class Car:
    def __init__(self, brand: str, model: str, mileage: int, year: int, price: float):
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.year = year
        self.price = price

    def display_info(self):
        return (f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, "
                f"Mileage: {self.mileage} km, Price: ${self.price:.2f}")
