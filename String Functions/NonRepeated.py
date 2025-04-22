string = input("Please Enter your text: ")
isNotRepeating = False
for i in string:
    if len(string.split(i)) > 2:
        pass
    else:
        print(f"{i} is the first Non-Repeating character in your text")
        isNotRepeating = True
        break

if not isNotRepeating:
    print("There is no character in your text that is not repeated.")
