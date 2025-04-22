text = input("Please Enter your text: ")
reversed_text = ""
for i in range(1, len(text)+1):
    reversed_text += text[0-(i)]
print(reversed_text)
