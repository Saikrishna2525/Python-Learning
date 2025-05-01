number = int(input("Please Enter a number: "))
def factorial(num):
    if num == 0 or num == 1:
        return num
    else:
        return num*factorial(num-1)
print(factorial(number))
