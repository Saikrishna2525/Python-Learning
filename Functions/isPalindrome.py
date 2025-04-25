text = input("Please Enter your word: ").lower()
textlist = []
listify = [lambda i=i: textlist.append(i) for i in text]
for i in listify:
    i()
textlist_COPY = textlist.copy()
textlist_COPY.reverse()
revtext = ""
for i in textlist_COPY:
    revtext += i
isPalindrome = lambda : True if text == revtext else False
print(isPalindrome())
