import math

def solution():
    num = ""
    i = 0
    while len(num) < 1_000_001:
        num += str(i)
        i += 1
    j = 1
    result = 1
    while j <= 1_000_000:
        result *= int(num[j])
        j *= 10
    return result

print(f"{solution():,}")