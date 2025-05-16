from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGODB_URL")
client = MongoClient(MONGO_URL)
db = client.Login_Simulator

admins = db.admin_data
pupils = db.student_data
