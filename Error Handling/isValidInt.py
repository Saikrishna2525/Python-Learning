from os import system
try:
    system('cls')
    notValidNumber = True
    while notValidNumber:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            system('cls')
            print("Value must be number!!!")
        else:
            notValidNumber = False
    print(f"Your number is {num}")
except KeyboardInterrupt:
    print("File Interrupted!!")
