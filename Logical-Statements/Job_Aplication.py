# Check Eligibility

age = int(input("Please enter your age: "))
experience = int(input("How much years of experience do you have: "))
skill = input("What is your skill: ")
eligible = (age >= 21) and (experience >= 2) and (skill.lower() == "python")

if eligible:
    print("You are eligible for developer role")
else:
    print("Sorry!, You are not eligible for develper role.")
