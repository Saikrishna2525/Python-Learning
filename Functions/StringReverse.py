def Reverse(str):
    return (str if len(str) <= 1 else (str[-1] + Reverse(str[:-1])))
print(Reverse(input("Enter your text: ")))
