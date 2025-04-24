Data = {
    "stock": {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "mango": 3
    },
    "orders": ["apple", "banana", "banana", "mango", "mango", "mango", "mango", "grape"]
}



for i in Data["orders"]:
    match i:
        case i if i in list(dict(Data["stock"]).keys()):
            match dict(Data["stock"])[i]:
                case j if j > 0:
                    j -= 1
                    print(f"Ordering of {Data["orders"] [(list(Data["orders"])).index(i)]} was successful!")
                case _:
                    print(f"{list(Data["orders"])[i]} is out of stock!")
                    pass
        case _:
            print(f"{list(Data["orders"])[i]} is not available!")
            pass
