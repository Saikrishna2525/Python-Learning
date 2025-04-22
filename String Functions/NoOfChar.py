string = input("Enter Your String: ").lower()
frequency = {}
for i in string:
    if i not in frequency:
        if i != "\t":
            frequency[i] = string.count(i)
        elif i == "\t":
            frequency["Tab"] = string.count("\t")
        elif i == "\ ":
            frequency["\ "] = string.count("\ ")
print(frequency)
