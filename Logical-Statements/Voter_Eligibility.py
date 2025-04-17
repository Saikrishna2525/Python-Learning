name = input("Please Enter your name: ")
age = int(input(f"Hi {name}! Please Enter your age: "))
if age > 18:
    print(f"{name} is eligible to vote.")
elif age < 18:
    print(f"{name} is underaged, wait for a few more years.")
else:
    print(f"{name} is a child, focus on studies!")

