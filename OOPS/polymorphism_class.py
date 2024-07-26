class Car:
    def __init__(self,brand) -> None:
        self.brand = brand
    def how_it_moves(self):
        print("Drive")
class Bike:
    def __init__(self,brand) -> None:
        self.brand = brand
    def how_it_moves(self):
        print("Ride")
class Boat:
    def __init__(self,brand) -> None:
        self.brand = brand
    def how_it_moves(self):
        print("Sail")

car =  Car("Ford")
bike = Bike("Honda")
boat = Boat("Mistibuishi")
for x in (car,bike,boat):
    x.how_it_moves()