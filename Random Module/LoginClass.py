from random import randint
import OTP_Generator
class User():
    def __init__(self, username: str, password: str):
        self.username=username
        self.password=password
    def login(self):
        username = input("Please Enter your username: ")
        password = input("Please Enter your password: ")
        if username != self.username or password != self.password:
            print("Incorrect Username or Password!")
        else:
            print("Correct Username and Password!")
            print(f"A four digit OTP will be sent to {self.username} through mail.")
            OTP = str(OTP_Generator.generateOTP())
            print("-------------------------------------------------")
            print("YOUR MAIL...")
            print(f"Hi {self.username}, Your OTP will be {OTP}")
            print("-------------------------------------------------")
            for i in range(6):
                User_OTP_Input = input("Please Enter your OTP: ")
                if User_OTP_Input != OTP and i != 5:
                    print("Your OTP is wrong!")
                elif i == 5 and User_OTP_Input != OTP:
                    print("You are out of chances!")
                else:
                    print("OTP Login Successful!")
                    break
    def logout(self):
        print(f"Sucessfully Logged Out {self.username}")
Person = User("Saikrishna25", "Secret123")
Person.login()
