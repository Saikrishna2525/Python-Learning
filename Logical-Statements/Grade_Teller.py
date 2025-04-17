# Grade Teller

marks = []
grade = ""
sum = 0
subject_count = int(input("How many subjects? \n"))
for i in range(subject_count):
    mark = float(input("Enter the marks ot of 100 : "))
    if mark < 35:
        grade = "Fail"
    marks.insert(0, mark)
if grade == "":
    for i in marks:
        sum += i
    average = sum / subject_count
    if average >= 90:
        grade = "A+"
    elif average >= 80 and average <= 89:
        grade = "A"
    elif average >= 70 and average <= 79:
        grade = "B"
    elif average >= 60 and average <= 69:
        grade = "C"
    elif average >= 50 and average <= 59:
        grade = "D"
    else:
        grade = "Fail"

print(f"Your grade is {grade}.")