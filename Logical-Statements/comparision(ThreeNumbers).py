# Find the largest of three numbers. 
num1 = int(input("Please Enter your first number: "))
num2 = int(input("Please Enter your second number: "))
num3 = int(input("Please Enter your third number: "))

maxValue = None
if num1 > num2 and num1 > num3:
    maxValue = num1
elif num2 > num1 and num2 > num3:
    maxValue = num2
elif num3 > num1 and num3 > num2:
    maxValue = num3
elif num1 == num2 == num3:
    print("All three numbers are equal.")

if maxValue != None:
    print(f"{maxValue} is greater than the other numbers")
