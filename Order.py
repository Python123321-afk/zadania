import Customer,Car
from datetime import datetime
class Order:
    def __init__(self, customer: Customer ,car: Car, date_start: datetime, date_finish: datetime):
        self.customer=customer
        self.car=car
        self.date_start=date_start
        self.date_finish=date_finish
    def display_info(self):
         print(f"surname: {self.customer.surname}, adress: {self.customer.adress} brand: {self.car.brand}, Model: {self.car.model}, Price: ${self.car.price:.2f}, date start: {self.date_start}, date finish: {self.date_finish}")
        
