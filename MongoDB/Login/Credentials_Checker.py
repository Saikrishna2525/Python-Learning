from tkinter import simpledialog, messagebox
from db_collections import pupils, admins

def password_validator(password: str):
    isLengthValid = len(password) > 8
    global isNotUsedCommonWords
    isNotUsedCommonWords = True
    commonWords = ["123", "100", "password", "pass", "2025", "me", "admin"]
    for Word in commonWords:
        if Word in password:
            isNotUsedCommonWords = False
            break
    return isLengthValid and isNotUsedCommonWords

def ask_username():
    while True:
        New_Username = simpledialog.askstring(
            title="Username", prompt="Please Enter your username"
        )
        pupil_exists = pupils.find_one({"Username": New_Username})
        admin_exists = admins.find_one({"Username": New_Username})
        if not pupil_exists and not admin_exists and New_Username:
            break
        elif New_Username == None:
            messagebox.showinfo("Terminated", "Account Creation Canceled!")
            exit()
        elif not New_Username:
            messagebox.showwarning("Username Error", "Username cannot be empty")
        else:
            messagebox.showwarning("Username Error", "Username already taken")
    return New_Username
