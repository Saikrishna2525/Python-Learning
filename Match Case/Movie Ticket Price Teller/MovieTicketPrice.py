import MovieTicketPriceData as Data
from os import system
system("cls")
Dimension = input("In Which Dimension Do you want to watch the movie (2D/3D): ").lower().strip()
Age = int(input("Please Enter your age: "))
isMember = input("Do you have a membership? (y/n): ").lower().strip()
Price = 0
match Dimension:
    case "2d":
        match Age:
            case age if age < 18:
                Price = Data.system_data["2d"]["Child"]
            case age if age >= 18 and age <= 60:
                Price = Data.system_data["2d"]["Adult"]
            case age if age > 60:
                Price = Data.system_data["2d"]["Senior Citizen"]
            case _:
                Price = "Invalid Age"
    case "3d":
        match Age:
            case age if age < 18:
                Price = Data.system_data["3d"]["Child"]
            case age if age >= 18 and age <= 60:
                Price = Data.system_data["3d"]["Adult"]
            case age if age > 60:
                Price = Data.system_data["3d"]["Senior Citizen"]
            case _:
                Price = "Invalid Age"
    case _:
        Price += "\nInvalid Dimension"

match isMember:
    case "y":
        Final_Price = Price * Data.Membership_Discount
    case "n":
        Final_Price = Price
    case _:
        Price += "\nInvalid Answer for is Membership"

system("cls")
print("                       Bill")
print("======================================================")
print(f"-> Movie Name : (Movie Name) in {Dimension.upper()}")
print(f"-> Price: {Price}")
print(f"-> Discount: {(Data.Membership_Discount * 100) if isMember == "y" else 0}%")
print(f"-> Total Price: {Final_Price}")
print("======================================================")
