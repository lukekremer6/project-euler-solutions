import math

def solution():
    BOUND = 12_000
    return sum(
        1
        for d in range(2, BOUND + 1)
        for n in range(d // 3 + 1, math.ceil(d / 2))
        if math.gcd(n, d) == 1
    )

print(f"{solution():,}")