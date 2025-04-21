string = input("Please Enter your text: ")
Swapped_Case = ""
letter = ""
for i in string:
    if i.isalpha():
        if i.islower():
            letter = i.upper()
            Swapped_Case += letter
        elif i.isupper():
            letter = i.lower()
            Swapped_Case += letter
    else:
        Swapped_Case += i
print(Swapped_Case)
