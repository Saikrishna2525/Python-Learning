number = int(input("Please Enter a number: "))
reverse_numbers = []
numbers = []
for i in str(number):
    reverse_numbers.insert(0, i)
    numbers.append(i)
if numbers == reverse_numbers:
    print("Your number is Palindrome.")
else:
    print("Your number is not Palindrome.")
