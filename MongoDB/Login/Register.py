from tkinter import simpledialog, messagebox
from db_collections import pupils, admins
from Credentials_Checker import *
from Login_Terminator import CheckNone
from dotenv import load_dotenv
import os

load_dotenv()
ADMIN_ID = os.getenv("ADMIN_ID")


def createAccount(isStudent=False):
    global isAdmin
    isAdmin = False
    New_Username = ""
    New_Username = ask_username()
    while True:
        New_Password = simpledialog.askstring(
            "Password", "Please Enter your password for the account.", show=chr(8226)
        )
        if New_Password == None:
            messagebox.showinfo("Terminated", "Account Creation Canceled!")
            exit()
        elif password_validator(New_Password):
            break
        else:
            messagebox.showwarning("Password Error", "Password Too Weak")
    if not isStudent:
        has_requested_admin = messagebox.askyesno(
            "Admin Access", "Do you want admin access?"
        )
        if has_requested_admin:
            inputAdminID = simpledialog.askstring(
                "Admin ID", "Please Enter the top secret admin ID", show=chr(8226)
            )
            isAdmin = False
            if inputAdminID == ADMIN_ID:
                isAdmin = True
                messagebox.showinfo(title="Success", message="Admin Access Granted")
            else:
                messagebox.showwarning(title="Denied", message="Access Denied!")
                isAdmin = False
    Name = simpledialog.askstring(title="Name", prompt="What Should We call you?")
    CheckNone(Name)
    Grade = simpledialog.askinteger(
        title="Class", prompt="Which grade are you studying?"
    )
    CheckNone(Grade)
    Age = simpledialog.askinteger(title="Age", prompt="How old are you?")
    CheckNone(Age)
    Course = simpledialog.askstring(
        title="Course", prompt="Which Course Are you joining?"
    )
    CheckNone(Course)
    UserAccountData = {
        "Username": New_Username,
        "Password": New_Password,
        "Name": Name,
        "Grade": Grade,
        "Age": Age,
        "Course": Course,
    }
    if isAdmin:
        res = admins.insert_one(UserAccountData)
        if res.inserted_id == None:
            print("An Error Occered!")
    else:
        res = pupils.insert_one(UserAccountData)
        if res.inserted_id == None:
            print("An Error Occured!")
    return UserAccountData
