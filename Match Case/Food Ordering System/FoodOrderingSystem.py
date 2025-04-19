import FoodOrderingSystemData as Data
# Food Ordering with Categories                                                   
# Task: Select food type → then choose item like veg idli - result as price , non veg chicken show result

Food_Type = input("Enter Food Type (Veg/Non-Veg): ").lower().strip()
Food = input("What Food Do you want: ").lower().strip()

def get_price():
    return Data.menu[Food_Type][Food]

Price = f"{Food} is currently not available."
match Food_Type:
    case "veg" | "non-veg":
        match Food:
            case type if type in Data.menu[Food_Type].keys():
                Price = get_price()
    case _:
        print("Invalid Foodtype!")

