number = int(input("Please Enter a number: ")) # 9875
while True:
    sum = 0
    for i in str(number):
        sum += int(i)
    if len(str(number)) == 1:
        break
    else:
        number = sum
print(f"The sum of the digits in your number until single digit is {sum}.")
