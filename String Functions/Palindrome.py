text = input("Please Enter your text: ").lower()
reversed_text = ""
for i in range(1, len(text)+1):
    reversed_text += text[0-(i)]
if reversed_text == text:
    print("Your text is palindrome!")
else: 
    print("Your text is not palindrome!")
