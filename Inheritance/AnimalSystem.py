class Animal():
    def sound(self):
        print("Make Sound...")
class Mammal(Animal):
    def giveBirth(self):
        print("Gave birth")
class Dog(Mammal):
    def sound(self):
        print("Bark! Bark! Bark!")
