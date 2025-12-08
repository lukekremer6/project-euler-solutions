import math

def solution():
    return sum(
        1
        for n in range(1, 101)
        for r in range(0, n + 1)
        if math.comb(n, r) > 1_000_000
    )

print(f"{solution():,}")