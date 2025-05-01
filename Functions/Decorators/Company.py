username = input("Please Enter your username: ")
details = input("Please Enter your Company Details: ")
competition = input("Please Enter the name of the Competition: ")
review_star_count = int(input("On a scale of 1 to 5. How much would you rate your experience: "))
experience = input("What was your experience visiting this place: ")
def speak1(func):
    def inner():
        print(f"Welcome to our company {username}.")
        func()
        print(f"Thank you, {username} for collaborating with us, all the best for your future endevours")
    return inner

@speak1
def speak2():
    print(f"Thanks for choosing our company, {username}")
    print(f"Your Review Star please?: Sure here is my rating, {review_star_count} star(s)")
    print(f"How was your experience being here {username}?: Ok, {experience}")
speak2()
