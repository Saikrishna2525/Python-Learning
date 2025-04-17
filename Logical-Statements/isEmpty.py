# Determine if a string is empty. 
text = input("Please Enter your text: ").strip()
if bool(text):
    print("Your text contains characters.")
else:
    print("Your text doesn't contain characters.")


# text="      hello    "
# trimmed=text.strip()

# print(trimmed)