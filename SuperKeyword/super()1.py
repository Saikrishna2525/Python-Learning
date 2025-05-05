class A():
    def __init__(self, name, date_modified):
        self.name=name
        self.date_modified=date_modified
    def display(self):
        print(self.__dict__)
class B(A):

    def __init__(self, name, date_modified):
        super().__init__(name, date_modified)
obj=B("Name", "Date_Modified")
obj.display()
