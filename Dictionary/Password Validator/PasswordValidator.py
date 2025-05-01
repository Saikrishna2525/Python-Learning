from Passwords import Passwords
from os import system
system("cls")
isLooping = True
while isLooping:
        print(f'{"Welcome Back":^50}')
        Username = input("Please Enter your username: ")
        if Username not in Passwords.keys():
            system("cls")
            print("Username not found!")
            isLooping = True
        else:
            isLooping = False
Status = "Crct"
for i in range(3):
    system("cls")
    print(f'{"Welcome Back":^50}')
    if Status == "Wrng":
         print("Incorrect Password!")
    print(f"Please Enter your username: {Username}")
    User_Password = input("Please Enter your password: ")
    if User_Password != Passwords[Username]:
        Status = "Wrng"
    elif User_Password == Passwords[Username]:
        
        print("Login Successful")
        Status = "Crct"
        
        break
if Status == "Wrng":
    print("Sorry, you can't login anymore due to 3 wrong passwords. \nThis suspicious attempt made the system block you from logging in.")
if Status == "Crct":
    print(f"Hello, {Username}.")
