class Vehicle():
    def start(self):
        print("Vehicle Started...")
class Car(Vehicle):
    def start(self):
        print("Car Started...")
car = Car()
car.start()
