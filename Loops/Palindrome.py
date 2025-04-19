number = int(input("Please Enter a number: "))
reverse_numbers = []
for i in str(number):
    reverse_numbers.append(i)
numbers = reverse_numbers.copy()
reverse_numbers.reverse()
if numbers == reverse_numbers:
    print("Your number is Palindrome.")
else:
    print("Your number is not Palindrome.")
