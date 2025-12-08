import functools
import itertools

def pentagonal_number(n):
    return n * (3 * n - 1) // 2

# Used to convert a sequence from the form 0, 1, 2, 3,... to 1, -1, 2, -2,...
def alternating_range(n):
    return (-1)**n * ((n + 2) // 2)

@functools.cache
def num_partitions(n):
    if n == 0:
        return 1
    result = 0
    for i in itertools.count():
        p = pentagonal_number(alternating_range(i))
        sign = -1 if i % 4 == 2 or i % 4 == 3 else 1
        if n < p:
            break
        result += sign * num_partitions(n - p)
    return result

def solution():
    TARGET = 1_000_000
    for n in itertools.count():
        if num_partitions(n) % TARGET == 0:
            return n

print(f"{solution():,}")