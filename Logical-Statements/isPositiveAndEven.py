# Check if a number is positive and even. 
int = int(input("Enter an integer: "))
if int > 0 and int % 2 == 0:
    print(f"{int} is Positive and Even")
elif (int < 0) and int % 2 == 0 and (int != 0):
    print(f"{int} is Even, but Negative.")
elif int > 0 and int % 2 != 0:
    print(f"{int} is Positive, but odd.")
elif not (int > 0 and int % 2 == 0) and (int != 0):
    print(f"{int} is Negative and odd.")
elif int == 0:
    print("Your number is only Even as your number is 0")
