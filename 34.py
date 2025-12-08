import math

factorials = [math.factorial(i) for i in range(10)]

def sum_of_factorial_digits(n):
    result = 0
    while n:
        result += factorials[n % 10]
        n //= 10
    return result

def solution():
    return sum(
        i for i in range(10, 3_000_000)
        if sum_of_factorial_digits(i) == i
    )

print(f"{solution():,}")