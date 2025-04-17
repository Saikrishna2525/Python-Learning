from os import system
answer = 0
Operators = ["+", "-", "/", "x", "^", "floor"]
isLooping = True
while True:
    while isLooping:
        operator = input("Enter your operator (+, -, /, x, ^, floor) and q to quit: ").lower()
        if operator not in Operators:
            system("cls")
            print("Invalid Operator!!!")
        else:
            isLooping = False
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    if operator == "+":
        answer = value1 + value2
    elif operator == "-":
        answer = value1 - value2
    elif operator == "/":
        answer = value1 / value2
    elif operator == "x":
        answer = value1 * value2
    elif operator == "^":
        answer = value1 ** value2
    elif operator == "floor":
        answer = value1 // value2
    elif operator == "q":
        print("Thank you, for using calculator!")
        exit(3)
    else:
        print("Invalid Operator!!!")
    print(f"The Answer is {answer}")
    

