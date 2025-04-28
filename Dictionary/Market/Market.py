from MarketInfo import Data
for i in Data["orders"]:
    match i:
        case i if i in list(dict(Data["stock"]).keys()):
            match dict(Data["stock"])[i]:
                case j if j > 0:
                    j -= 1
                    print(f"Order successful!")
                case _:
                    print(f"Out of stock!")
                    pass
        case _:
            print(f"Item not available!")
            pass
