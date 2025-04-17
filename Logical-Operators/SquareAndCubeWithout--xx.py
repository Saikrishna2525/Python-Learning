from os import system
while True:
    MainNum = input("Do you want the square of a number or the cube of a number (s/c): ").lower()
    if MainNum in ["s", "c"]:
        break
    else:
        system("cls")
        print("Invalid Choice!")

num1 = int(input("Please Enter a Number: "))
if MainNum == "s":
    Answer = num1 * num1
elif MainNum == "c":
    Answer = num1 * num1 * num1

print(f"The Answer is {Answer}. ")
