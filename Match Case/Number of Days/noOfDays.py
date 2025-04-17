from noOfDaysData import month_data
month = input("Enter the current month in short (like Jan for January): ")
match month.lower().strip():
    case month if month in month_data:
        print(f"The given month has {month_data[month]} days.")
    case _:
        print("Please Enter a valid month!")
