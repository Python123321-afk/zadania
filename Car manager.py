import Car
class Car_manager:
    cars=[]
    def add_cars(self,Marka,Model,Przebieg,Rok_produkcji,cena):
        self.cars.append(Car(Marka,Model,Przebieg,Rok_produkcji,cena))
    def update_car(self,cena,model):
        for i in self.cars:
            if i.model==model:
                i.cena = cena
                



        