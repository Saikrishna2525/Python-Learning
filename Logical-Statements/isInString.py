# Check if a string contains a specific substring. 
string = input("Enter the text: ")
substring = input("Enter the text which you want to check if it is there in the first string: ")
if substring in string:
    print(f"{substring} is a substring of {string}.")
else:
    print(f"{substring} is not a substring of {string}.")
