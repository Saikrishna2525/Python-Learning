number = int(input("Enter your number: "))
def sumOfnumberbers(num):
    if num==1:
        return 1
    else:
        return num+sumOfnumberbers(num-1)
print(sumOfnumberbers(number))
