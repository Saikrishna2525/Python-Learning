path = r"OrigData.txt"
with open(path, "r") as victim:
    ClonedData = victim.read()
with open("Cloned.txt", "x") as Clone:
    Clone.write(ClonedData)