number = int(input("Please Enter a number: "))
print("For Loop...")
for i in reversed(str(number)):
    print(i, end="")
print()
print("While Loop...")
i = len(str(number)) - 1
while i != -1:
    print(str(number)[i], 
          end="")
    i -= 1