def student_info(*nameAge, **rank):
    name = nameAge[0]
    age = nameAge[1]
    ranks = rank.get("grade", "Unknown")
    return f"Name: {name}, Age: {age}, Grade: {ranks}"
print(student_info("Sai", 11, grade="A"))