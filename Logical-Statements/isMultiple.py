# Check if a given number is a multiple of 3 and 7. 
number = int(input("Enter a number: "))
if number % 3 == 0:
    if number % 7 == 0:
        print(f"{number} is divisible by 3 and 7.")
    else:
        print(f"{number} is divisible by 3, but not by 7")
if number % 7 == 0 and number % 3 != 0:
    print(f"{number} is divisible by 7, but not by 3")
if number % 7 != 0 and number % 3 != 0:
    print(f"{number} is not divisible by 3 and 7")
