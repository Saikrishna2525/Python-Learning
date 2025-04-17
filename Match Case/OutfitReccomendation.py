season = input("Enter the current season: ")
match season:
    case "Winter":
        print("Wear woolen clothes for this Winter for resisting the cold environent.")
    case "Summer":
        print("Don't wear woollen clothes this summer.")
    case _:
        print("Enter a valid season.")
