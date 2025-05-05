class Person():
    def __init__(self, name):
        self.name=name
    def get_info(self):
        return self.__dict__
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade=grade
obj=Student("Sai", 6)
print(obj.get_info())

