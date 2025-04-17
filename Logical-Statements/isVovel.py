# Check if a character is a vowel. 
vovels = ["a", "e", "i", "o", "u"]
letter = input("Enter a letter: ").lower()
if letter in vovels:
    print(f"{letter} is a vovel")

elif not letter.isdigit() and len(letter) > 1:
    print("Letter cannot be more than one character")

elif letter not in vovels and not letter.isalpha:
     print(f"{letter} is a consonant")


# else:
#     print(f"{letter} is a consonant")