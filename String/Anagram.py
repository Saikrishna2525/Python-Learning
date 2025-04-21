string1 = input("Enter your text: ")
string2 = input("Enter your text: ")
if sorted(string1.lower()) == sorted(string2.lower()):
    print("Your words are Anagrams!")
else:
    print("Your words are not Anagrams!")
