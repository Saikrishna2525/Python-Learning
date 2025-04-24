from Passwords import Passwords

for i in range(3):
    isLooping = True
    while isLooping:
        
        print(f'{"Welcome Back":^50}')
        Username = input("Please Enter your username: ")
        if Username not in Passwords.keys():
            
            print("Username not found!")
            
        else:
            isLooping = False
    User_Password = input("Please Enter your password: ")
    if User_Password != Passwords[Username]:
        
        print("Incorrect Password!")
        
        Status = "Wrng"
    elif User_Password == Passwords[Username]:
        
        print("Login Successful")
        Status = "Crct"
        
        break
if Status == "Wrng":
    print("Sorry, you can't login anymore due to 3 wrong passwords. \nThis suspicious attempt made the system block you from logging in.")
if Status == "Crct":
    print(f"Hello, {Username}.")