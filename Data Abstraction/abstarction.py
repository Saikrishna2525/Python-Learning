from abc import ABC, abstractmethod
class Bus(ABC):
    def __init__(self, number_plate: str):
        self.number_plate=number_plate
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def horn(self):
        pass        
# obj = Bus("9876546331") # I have Inherited ABC so you can't create an object called bus
# obj.move() # Won't Reach Here because of an error on the previous line
# These Can't be used anywhere except by another class which inherits Bus 
class CityBus(Bus):
    def __init__(self, number_plate: str):
        super().__init__(number_plate)
    def move(self):
        print("Moving...")
    def horn(self):
        print("Beep!...Beep!")
bus1 = CityBus("A0J81JS92JD")
bus1.move() # This Works
