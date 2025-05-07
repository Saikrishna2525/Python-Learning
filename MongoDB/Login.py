from pymongo import MongoClient
from dotenv import load_dotenv
from random import randint
import os

print("Please Wait...")
load_dotenv()
MONGO_URL = os.getenv("MONGODB_URL")
client = MongoClient(MONGO_URL)

username = "SaiKrishna2525"
password = "Secure123"

db = client.login_simulator
col1 = db.Logins
otp = str(randint(1000, 9999))
col1.delete_many({})
loginData = {
    "USERNAME":username,
    "PASSWORD":password,
    "OTP":otp
}
res = col1.insert_one(loginData)
res.inserted_id

os.system("cls" if os.name == "nt" else "clear")
inputUsername = input("Please Enter your username: ")
inputPassword = input("Please Enter your password: ")
os.system("cls" if os.name == "nt" else "clear")
print(f"Please Enter your username: {inputUsername}")
print(f"Please Enter your password: {chr(8226) * len(password)}")
MongoOTP = col1.find_one({"OTP":{"$exists":True}})
MongoUsername = col1.find_one({"USERNAME":{"$exists":True}})
MongoPassword = col1.find_one({"PASSWORD":{"$exists":True}})
if inputPassword != MongoPassword["PASSWORD"] or inputUsername != MongoUsername["USERNAME"]:
    print("Incorrect Username or Password!")
else:
    inputOTP = input("Enter the 4 digit OTP sent to you: ")
    if inputOTP == MongoOTP["OTP"]:
        print("Successfully Logged in via OTP Authentication!")
    else:
        print("Incorrect OTP!")
