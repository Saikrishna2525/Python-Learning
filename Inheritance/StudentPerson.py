class Person():
    def __init__(self, name, age, gender, occupation):
        self.name=name
        self.age=age
        self.gender=gender
        self.occupation=occupation
    def activities(self):
        pass
class Student(Person):
    def __init__(self, name, age, gender, occupation, activity):
        super().__init__(name, age, gender, occupation)
        self.activity=activity
    def activities(self):
        print(f"{self.activity}ing")        
