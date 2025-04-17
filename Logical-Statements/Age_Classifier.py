# ● Ask for age 
# ● Classify as: 
# ○ Age < 13 → "Child" 
# ○ Age 13–19 → "Teen" 
# ○ Age 20–59 → "Adult" 
# ○ Age 60+ → "Senior Citizen" 

age = int(input("Please Enter your age: "))
if age < 13:
    classify = "Child"
elif age >= 13 and age <= 19:
    classify = "Teen"
elif age >= 20 and age <= 59:
    classify = "Adult"
elif age >= 60:
    classify = "Senior Citizen"
else:
    pass
print(f"You are a {classify}.")
