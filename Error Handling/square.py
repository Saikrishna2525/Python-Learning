try:
    number = int(input("Enter a number: "))
    print(f"Square of {number} is {number**2}")
except Exception as Exception:
    print(f"An Error Occured {Exception}")
else:
    print("Success...!")