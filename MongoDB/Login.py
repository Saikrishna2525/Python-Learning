from pymongo import MongoClient
from dotenv import load_dotenv
from random import randint
from 
import os

load_dotenv()
MONGO_URL = os.getenv("MONGODB_URL")
client = MongoClient(MONGO_URL)

username = "SaiKrishna2525"
password = "Secure123"

db = client.login_simulator
col1 = db.Logins
otp = randint(1000, 9999)
loginData = {
    "USERNAME":username,
    "PASSWORD":password,
    "OTP":otp
}
res = col1.insert_one(loginData)
print(res.inserted_id)

inputUsername = input("Please Enter your username: ")
inputPassword = input("Please Enter your password: ")
if inputPassword != password or inputUsername != username:
    print("Incorrect Username or Password!")
else:

