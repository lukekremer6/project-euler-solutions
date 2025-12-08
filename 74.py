import math

def sum_of_factorial_of_digits(n):
    return sum(math.factorial(int(digit)) for digit in str(n))

def has_chain_length_60(n):
    chain = set()
    while n not in chain:
        chain.add(n)
        n = sum_of_factorial_of_digits(n)
    return len(chain) == 60

def solution():
    return sum(1 for i in range(1_000_000) if has_chain_length_60(i))

print(f"{solution():,}")