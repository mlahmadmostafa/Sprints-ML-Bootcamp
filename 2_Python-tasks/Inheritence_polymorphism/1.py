class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("Car started")
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    def start(self):
        print("Electric car started")
car1 = Car("Toyota", "Camry", 2022)
car2 = ElectricCar("Tesla", "Model S", 2022)
car1.start()
car2.start()