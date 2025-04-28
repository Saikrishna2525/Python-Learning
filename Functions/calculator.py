def add_or_subtract(num1, num2, **sign):
    return ((num1 + num2) if sign.get("operator", "add").lower() == "add" else (num1 - num2 if sign.get("operator", "add").lower() == "subtract" else "Invalid Operator"))
print(add_or_subtract(3, 5))
