# Food Ordering with Categories                                                   
# Task: Select food type → then choose item like veg idli - result as price , non veg chicken show result

Food_Type = input("Enter Food Type (Veg/Non-Veg): ").lower().strip()
if Food_Type not in ("veg", "non-veg"):
    print("Invalid FoodType!")
else:
    exit(1)
