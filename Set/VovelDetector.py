vovels = {"a", "e", "i", "o", "u"}
sentence = input("Please Enter a Sentence: ").lower()
vovels_in_txt = set({})
for i in sentence:
    if i in vovels:
        vovels_in_txt.add(i)
if vovels_in_txt == vovels:
    print("Your text contains all vovels!")
else:
    print("Your text doesn't contain all vovels!")
