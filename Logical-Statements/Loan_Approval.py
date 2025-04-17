# ● Input: age, salary, credit score 
# ● If age ≥ 21 and salary ≥ 25000 and credit score ≥ 700 → "Loan Approved" ● Else → "Loan Denied" 

age = int(input("Please Enter your age: "))
salary = int(input("Please Enter your salary per annum: "))
credit_score = int(input("Please Enter your your credit score: "))

if (age >= 21) and (salary >= 25000) and (credit_score >= 700):
    print("Loan Approved")
else:
    print("Loan Denied")


