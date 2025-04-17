# ○ 5–11 → "Good Morning" 
# ○ 12–17 → "Good Afternoon" 
# ○ 18–20 → "Good Evening" 
# ○ 21–4 → "Good Night" 

Message = ""
hour = int(input("Please Enter the current hour: "))
if hour >= 5 and hour <= 11:
    Message = "Morning"
elif hour >= 12 and hour <= 17:
    Message = "Afternoon"
elif hour >= 18 and hour <= 20:
    Message = "Evening"
elif (hour >= 21 and hour <= 24) or (hour >= 1 and hour <= 4):
    Message = "Night"
else:
    print("Invalid Hour")

if Message == "":
    pass
else:
    print(f"Good {Message}")
