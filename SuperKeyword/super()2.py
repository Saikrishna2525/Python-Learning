class A():
    def __init__(self, name, date_modified):
        self.name=name
        self.date_modified=date_modified
    def display():
        print("Displayed...")
class B(A):
    def __init__(self, name, date_modified):
        super().__init__(name, date_modified)
class C(B):
    def __init__(self, name, date_modified):
        super().__init__(name, date_modified)
obj = C("Name", "Date")
