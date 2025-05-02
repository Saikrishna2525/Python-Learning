class Person():
    def activity(self):
        print("Activity...")
class Teacher(Person):
    def teach(self):
        print("Teaching...")
class Student(Person):
    def learn(self):
        print("Learning...")
class Assistant(Teacher, Student):
    pass
