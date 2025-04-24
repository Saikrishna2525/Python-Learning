PerA = {"Apple", "Orange", "Jackfruit","Mango"}
PerB = {"Bannana", "Orange", "Tomato", "Mango"}
UniqueB = PerA.difference(PerB)
UniqueA = PerB.difference(PerA)
print(f"Unique to Person A: {UniqueA}")
print(f"Unique to Person B: {UniqueB}")
