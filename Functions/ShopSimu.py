from os import system
# welcome to our shop

# what do you want?
# 1) Rice - 40Rs/kg
# 2) Sugar - 50Rs/Kg
# 3) Soap - 10Rs/piece
# Please select the which product do you need?

# if i select 1:
# you need to print "You selected rice"
# Q: How much rice do you nee?
# input: 2
# The cost of 2Kg rice is rs: 80
# Q: Give the amount: 
# input: 100
# you need to print "here the balance is 20Rs"

# Thank you 'visit again'
system("cls")
FoodData = {"rice":40, "sugar":50, "soap":10}
def buy(item, quantity):
    if item not in list(FoodData.keys()):
        print("Sorry, but, that item is not available on our store.")
        return None
    temp_item = item.lower()
    print(f"You Selected Rice!")
    print(f"The cost of {quantity}Kg or piece is ₹{FoodData[temp_item] * quantity}")
    print("Give me the money through PayTM")
    print("\t")
    print("To: Shopkeeper")
    MoneyNotEnough = True
    Selling_Price = int(input("How much money do you want to pay: ₹"))
    while MoneyNotEnough:
        if Selling_Price >= FoodData[temp_item] * quantity:
            print(f"Here, Take the change of ₹{Selling_Price - (FoodData[temp_item] * quantity)}")
            print("Thank you for visiting the store! Please Visit Again")
            MoneyNotEnough = False
        else:
            system('cls')
            print(f"Where is remaining ₹{(FoodData[temp_item] * quantity) - Selling_Price}")
            print("Pay That much money! NOW!")
            Selling_Price += int(input("How much money do you want to pay: ₹"))
item = input("Welcome To My Shop\nWhat do you want: ")
quantity = int(input(f"How many {item}s do you want?: "))
buy(item, quantity)
