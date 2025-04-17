from os import system
# 3)Electricity Bill Slab System
#    Units consumed:
#  0–100 → ₹3/unit
#  101–300 → ₹5/unit
# 301–500 → ₹7/unit
# 500 → ₹10/unit

system("cls")
Units_Consumed = int(input("How much units did your appliances consume: "))
system("cls")
match Units_Consumed:
    case units if units >= 0 and units <= 100:
        Cost = units * 3
    case units if units >= 101 and units <= 300:
        Cost = units * 5
    case units if units >= 301 and units <= 500:
        Cost = units * 7
    case units if units > 500:
        Cost = units * 10
    case _:
        Cost = "An Error Occured!"

print("============================================================")
print(f"-> Units Consumed: {Units_Consumed}")
print(f"-> Total: ₹{Cost}.00")
print("============================================================")
