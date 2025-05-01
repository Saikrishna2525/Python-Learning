class Student():
    def __init__(self, name, standard, age, PnNo, hobby):
        self.name=name
        self.standard=standard
        self.age=age
        self.PnNo=PnNo
        self.hobby=hobby
    def study(self):
        print("a² + b² = c²")
    def speak(self):
        print(f"Hi I'm {self.name}")
    def gaming(self):
        print("Gaming......")
    def set_info(self, name, standard, age, PnNo, hobby):
        self.name=name
        self.standard=standard
        self.age=age
        self.PnNo=PnNo
        self.hobby=hobby
    def get_info(self):
        return self.__dict__

Student1 = Student("Alice", 6, 11, 9876543210, "Coding")
