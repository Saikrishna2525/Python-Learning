import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 20]
prime_numbers = list(filter(is_prime, numbers))

print(prime_numbers)
