try:
    path = r"OrigData.txt"
    with open(path, "r") as victim:
        ClonedData = victim.read()
    with open("Cloned.txt", "x") as Clone:
        Clone.write(ClonedData)
except FileExistsError:
    print("Cloned file already exists")
