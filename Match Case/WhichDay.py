weekend = ["sunday", "saturday"]
weekday = ["monday", "tuesday", "wednesday", "thursday", "friday"]
day = input("What day is it today: ")
match (day.lower()).strip():
    case day if day in weekend:
        print("Today is a weekend.")
    case day if day in weekday:
        print("Today is a weekday.")
    case _:
        print("Please Enter a valid day!")
