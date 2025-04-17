# ● Input age of the customer. 
# ● Pricing rules: 
# ○ Age < 5 → "Free Ticket" 
# ○ Age 5–12 → ₹100 
# ○ Age 13–59 → ₹200 
# ○ Age 60+ → ₹120 (Senior citizen discount)

age = int(input("Please Enter your age: "))
if age < 5:
    price = 0
elif age >= 5 and age <= 12:
    price = 100
elif age >= 13 and age <= 59:
    price = 200
elif age >= 60:
    price = 120

input(f"Your ticket cost is rupees {price}")

