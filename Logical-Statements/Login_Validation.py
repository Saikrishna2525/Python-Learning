# ● Assume correct username: "admin", password: "1234" ● Input username and password from user 
# ● If both are correct → "Login Successful" 
# ● If username correct, password wrong → "Incorrect Password" ● If username wrong → "User not found"

correct_username = "admin"
correct_password = "1234"
username = input("Please Enter your Username: ")
password = input("Please Enter your password: ")

if (username, password) == (correct_username, correct_password):
    print("Login Successful!")
elif username == correct_username and password != correct_username:
    print("Incorrect Password!")
elif (username, password)!= (correct_username, correct_password):
    print("User not found!")
