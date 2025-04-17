# 2)Library Fine System
#    0 days late → No fine
#   1–5 days → ₹5/day
#   6–10 → ₹10/day

late = float(input("How many days was the person late for returning the book: "))
match late:
    case 0:
        print("You have no fine! 😃")
    case late if late >= 1 and late <= 5:
        print(f"Your fine is ₹{late * 5}")
    case late if late >= 6 and late <= 10:
        print(f"Your fine is ₹{late * 10}")
    case late if late > 10:
        print(f"Your fine is ₹{late * 50}. ☹️")
    case _:
        print("Enter a valid number")
