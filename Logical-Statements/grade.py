# Determine the grade based on marks. 
# ● 90 and above → Grade: A+ 
# ● 80 - 89 → Grade: A 
# ● 70 - 79 → Grade: B 
# ● 60 - 69 → Grade: C 
# ● 50 - 59 → Grade: D 
# ● Below 50 → Grade: Fail 

mark = int(input("Enter your marks out of 100: "))
if mark >= 90:
    grade = "A+"
elif mark >= 80 and mark <= 89:
    grade = "A"
elif mark >= 70 and mark <= 79:
    grade = "B"
elif mark >= 60 and mark <= 69:
    grade = "C"
elif mark >= 50 and mark <= 59:
    grade = "D"
else:
    grade = "Fail"

print(f"Your Grade is {grade}.")
