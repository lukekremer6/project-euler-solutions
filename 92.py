import functools

@functools.cache
def square_of_digits(n):
    return sum(int(digit)**2 for digit in str(n))

@functools.cache
def chain_end(n):
    return n if n == 1 or n == 89 else chain_end(square_of_digits(n))

def solution():
    BOUND = 10_000_000
    return sum(1 for n in range(1, BOUND) if chain_end(n) == 89)

print(f"{solution():,}")