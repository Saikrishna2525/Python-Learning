import json
infoPath1 = r"Student_Info/Student_Info.json"
infoPath2 = r"Student_Info/Student_Info_withGrade.json"
with open(infoPath1, 'r') as data1:
    info1 = json.load(data1)
with open(infoPath2, 'r') as data2:
    info2 = json.load(data2)
def StudentData(*nameAge, **alphabeticRank):
    if len(nameAge) != 2:
        return "Enter both name and age!"
    if alphabeticRank.get("grade", "Unknown") == "Unknown":
        Data = info1
        key = dict(Data.get(f"{nameAge[0]}, {nameAge[1]}"))
        return key if alphabeticRank["grade"] == key["grade"] else "Student Not Found!"
print(StudentData("Bob", 11, grade="B"))
