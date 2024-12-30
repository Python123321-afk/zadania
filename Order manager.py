import Order,Customer,Car
from datetime import datetime 
class Order_Manager:
    orders=[]
    def add_order(self,customer: Customer ,car: Car, date_start: datetime, date_finish: datetime):
        self.orders.append(Order(customer,car,date_start,date_finish))
    def get_historic_order(self):
        for i in self.orders:
            if i.date_finish<datetime.now():
                i.display_info()
    def get_future_order(self):
        for i in self.orders:
            if i.date_start>datetime.now():
                i.display_info()
    def get_car(self,date_start,date_finish):
        avaible_cars=[]
        for i in self.orders:
            if i.date_start<date_start and i.date_finish<date_start:
                avaible_cars.append(i.car)    
        return avaible_cars
        