from seasonData import *
month = input("Enter the current month: ")
match month.lower().strip():
    case month if month in Winter:
        print("It is Winter!!!")
    case month if month in Summer:
        print("It is summer!!!")
    case month if month in Monsoon:
        print("It is monsoon!!!")
    case month if month in Autumn:
        print("It is Autumn!!!")
    case _:
        print("Enter a valid month!!!")
