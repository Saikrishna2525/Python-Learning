N = int(input("N = "))
def count(n):
    temp = 1
    
    print(f"{n}, ", end="")
    if n != 0:
        count(n-1)
count(N)
