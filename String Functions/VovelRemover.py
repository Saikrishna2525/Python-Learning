string = input("Please Enter your text: ").lower()
vovels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for i in vovels:
    string = string.replace(i, "")
print(string)    
