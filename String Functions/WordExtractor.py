words = "Apple", "Bananna"
Letter = input("Please Enter a letter: ").capitalize()
if len(Letter) != 1:
    print("Your text is not a letter!")
else:
    for i in words:
        if i.startswith(Letter):
            print(i)
