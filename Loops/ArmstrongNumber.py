number = int(input("Enter a number: "))
cubes = []
for i in str(number):
    cubes.append(int(i) ** 3)
if sum(cubes) == number:
    print("Your number is an Armstrong Number.")
else:
    print("Your number is not an Armstrong Number.")
