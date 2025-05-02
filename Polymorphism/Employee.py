class Employee():
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def __init__(self, name, salary, property_department):
        super().__init__(name, salary)
        self.property_department=property_department
    def get_info(self):
        return self.__dict__
