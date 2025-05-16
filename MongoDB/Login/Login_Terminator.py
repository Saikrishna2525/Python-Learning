from tkinter import messagebox


def CheckNone(val, text="Account Creation Canceled!"):
    if val is None:
        messagebox.showinfo("Terminated", text)
        exit()
