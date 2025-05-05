import re
TelephoneNumber = input("Enter your telephone number: ")
print(re.findall(r"^[0-9]{3,}+-+[0-9]{10}$", TelephoneNumber))
