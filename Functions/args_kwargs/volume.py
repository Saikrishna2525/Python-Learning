def volume(shape, **type):
    if str(shape).lower() == "cube":
        return type["side"] ** 3
    elif str(shape).lower() == "sphere":
        return (4/3) * (22/7) * (type["radius"] ** 3)
print(volume("cube", side=3))
