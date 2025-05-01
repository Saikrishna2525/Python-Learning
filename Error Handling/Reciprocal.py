try:
    number = int(input("Please Enter a number: "))
except ValueError:
    print("Number must not be letters!!!")
else:
    try:
        print(f"Reciprocal of {number} is {number**-1}")
    except ZeroDivisionError:
        print("Number must not be 0")
