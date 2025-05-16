from pymongo import MongoClient
from dotenv import load_dotenv
from otpgenerator import specialOTP
from Login_Terminator import CheckNone
from Credentials_Checker import *
from Register import *
import os

isAdmin = False
os.system("cls" if os.name == "nt" else "clear")
load_dotenv()
MONGO_URL = os.getenv("MONGODB_URL")
ADMIN_ID = os.getenv("ADMIN_ID")
from db_collections import admins, pupils


def logined(data: dict):
    global CurrentUserInfo, isAdmin
    CurrentUserInfo = data
    isAdmin = CurrentUserInfo.get("isAdmin", False)
    while True:
        decision2 = simpledialog.askstring(
            "Dashboard",
            "What do you want to do? (Add, Update, View, Logout, See All Student Data, See All Admin Data or DELETE) your profile",
        )
        CheckNone(decision2, "Logging Out...")
        decision2 = decision2.lower().strip()
        isStudent = True
        if decision2 == "add":
            createAccount(isStudent=True)
        elif decision2 == "update":
            if isAdmin:
                res2 = dict(admins.find_one({"Username":CurrentUserInfo["Username"]}))
            else:
                res2 = dict(pupils.find_one({"Username":CurrentUserInfo["Username"]}))
            txt = ""
            for keys, values in res2.items():
                if keys == "_id":
                    continue
                txt += (f"{keys} : {values}" + "\n")
            txt += "What data do you want to change."
            # simpledialog.askstring("Your Data", txt)
            FieldToModify = simpledialog.askstring("Change Data", txt)
            CheckNone(FieldToModify, "Exiting...")
            FieldToModify = FieldToModify.lower().strip()
            if FieldToModify == "username":
                New_Username = ask_username()
                CheckNone(New_Username)
                if isAdmin:
                    res = admins.update_one({"Username":CurrentUserInfo["Username"]}, 
                                            {"$set":{"Username":New_Username}})
                else:
                    res = pupils.update_one({"Username":CurrentUserInfo["Username"]},
                                            {"$set":{"Username":New_Username}})
                CurrentUserInfo["Username"] = New_Username
                    

            if FieldToModify == "password":
                Old_Password = simpledialog.askstring("Password", "Please Enter your password.\nWhy are we asking this?\n(because cannot let others changing your password)", show=chr(8226))
                if Old_Password == CurrentUserInfo["Password"]:
                    while True:
                        New_Password = simpledialog.askstring("Password", "Please Enter your new password", show=chr(8226))
                        CheckNone(New_Password, "Exiting...")
                        if password_validator(New_Password):
                            break
                        else:
                            messagebox.showwarning("Password Error", "Password Too Weak!")
                    if isAdmin:
                        res = admins.update_one({"Username":CurrentUserInfo["Username"]},
                                                {"$set":{"Password":New_Password}})
                    else:
                        res = pupils.update_one({"Username":CurrentUserInfo["Username"]},
                                                {"$set":{"Password":New_Password}})
                else:
                    messagebox.showwarning("Incorrect Credentials!", "Incorrect Password or username!")
            if FieldToModify == "name":
                New_Name = simpledialog.askstring("Name", "Please Enter the new name")
                CheckNone(New_Name, "Exiting...")
                if isAdmin:
                    res = admins.update_one({"Username":CurrentUserInfo["Username"]},
                                            {"$set":{"Name":New_Name}})
                else:
                    res = pupils.update_one({"Username":CurrentUserInfo["Username"]},
                                            {"$set":{"Name":New_Name}})
            if FieldToModify == "grade":
                New_Grade = simpledialog.askinteger("Grade", "Enter new grade")
                CheckNone(New_Grade, "Exiting...")
                if isAdmin:
                    admins.update_one({"Username":CurrentUserInfo["Username"]},
                                    {"$set":{"Grade":New_Grade}})
                else:
                    pupils.update_one({"Username":CurrentUserInfo["Username"]},
                                    {"$set":{"Grade":New_Grade}})
            if FieldToModify == "age":
                New_Age = simpledialog.askinteger("Age", "Please Enter your new age.")
                CheckNone(New_Age, "Exiting...")
                if isAdmin:
                    admins.update_one({"Username":CurrentUserInfo["Username"]},
                                    {"$set":{"Age":New_Age}})
                else:
                    pupils.update_one({"Username":CurrentUserInfo["Username"]},
                                    {"$set":{"Age":New_Age}})
            if FieldToModify == "course":
                New_Course = simpledialog.askstring("Course", "What is your new course?")
                CheckNone(New_Course, "Exiting...")
                if isAdmin:
                    admins.update_one({"Username":CurrentUserInfo["Username"]},
                                    {"$set":{"Course":New_Course}})
                else:
                    pupils.update_one({"Username":CurrentUserInfo["Username"]},
                                      {"$set":{"Course":New_Course}})  

        elif decision2 == "view":
            if isAdmin:
                res2 = dict(admins.find_one({"Username":CurrentUserInfo["Username"]}))
            else:
                res2 = dict(pupils.find_one({"Username":CurrentUserInfo["Username"]}))
            txt = ""
            for keys, values in res2.items():
                if keys == "_id":
                    continue
                txt += (f"{keys} : {values}" + "\n")
            txt += "This is your current data"
            messagebox.showinfo("Your Data", txt)
        elif decision2 == "logout":
            break
        elif decision2 == "delete":
            confirmation = simpledialog.askstring("Confirmation", "Exactly type 'DELETE' for deleting this account!")
            if confirmation == 'DELETE':
                if isAdmin:
                    admins.delete_one({"Username":CurrentUserInfo["Username"]})
                else:
                    pupils.delete_one({"Username":CurrentUserInfo["Username"]})
                break
            else:
                messagebox.showerror("Canceled", "Deletion Canceled!")
        elif decision2 == "see all student data":
            if not isAdmin:
                messagebox.showwarning("Denied", "This is an admin only feature!")
            else:
                data = pupils.find(
                    {"Username":{"$regex":"."}},
                    {"_id":0}
                    )
                txt = ""
                for i in data:
                    txt += str(i)
                messagebox.showinfo("Student Data", txt)
        elif decision2 == "see all admin data":
            if not isAdmin:
                messagebox.showwarning("Denied", "This is an admin only feature!")
            else:
                data = admins.find({"Username":{"$regex":"."}})
                txt = ""
                for i in data:
                    txt += str(i)
                messagebox.showinfo("Student Data", txt)
    begin_choice()

def begin_choice():
    global isAdmin, doesUsernameExists
    decision = simpledialog.askstring(
    "Create or Login to Existing",
    "Do you want to create account or log in to existing account. (Create/Existing)",
    )
    CheckNone(decision, "Exiting...")
    decision = decision.lower().strip()
    doesUsernameExists = True
    if decision == "create" or decision == "make" or decision == "makeaccount":
        doesUsernameExists = False
        res = createAccount()
        logined(res)
    if decision == "exist" or decision == "existing" or decision == "isthere":
        Old_Username = simpledialog.askstring("Username", "Please Enter your username:")
        DataForLoggingIn = pupils.find_one({"Username":Old_Username})
        if DataForLoggingIn == None:
            DataForLoggingIn = admins.find_one({"Username":Old_Username})
            if DataForLoggingIn == None:
                doesUsernameExists = False
                DataForLoggingIn = dict({})
                DataForLoggingIn["Password"] = "\u0000"
            else:
                isAdmin = True
                DataForLoggingIn["isAdmin"] = True
        Old_Password = simpledialog.askstring("Password", "Please Enter your password", show=chr(8226))
        if Old_Password == DataForLoggingIn["Password"]:
            logined(DataForLoggingIn)
        else:
            if doesUsernameExists:
                messagebox.showwarning("Incorrect Credentials!", "Incorrect Password or Username!")
            else:
                messagebox.showerror("Username Error", "Username Does not exist!\nbut you can create it.")
                begin_choice()
begin_choice()
