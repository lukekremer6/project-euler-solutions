import math

def euclid_formula(m, n):
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2
    return a, b, c

def perimeter(m, n):
    a, b, c = euclid_formula(m, n)
    if abs(c - a * 2) == 1:
        return 2 * (a + c)
    if abs(c - b * 2) == 1:
        return 2 * (b + c)
    return 0

def solution():
    BOUND = 10**9

    return sum(
        perimeter(m, n)
        for n in range(1, math.ceil(math.sqrt((3 * BOUND - 11) / 12) - 1 / 2))
        for m in range(n + 1, math.ceil(math.sqrt(BOUND / 3 - n**2)), 2)
        if math.gcd(m, n) == 1
    )

print(f"{solution():,}")