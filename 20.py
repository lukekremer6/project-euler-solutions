import math

def sum_of_digits(n):
    s = str(n)
    return sum(int(digit) for digit in s)

def solution():
    x = math.factorial(100)
    return sum_of_digits(x)

print(solution())