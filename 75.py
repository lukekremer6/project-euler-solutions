import math
import itertools

# Use Euclid's formula to generate Pythogorean triples.
# We can place an upper bound on m and n.
# We know b < L / 2 and b = 2 * m * n.
# So n < L / 4 * m and m < L / 4 * n.
# The smallest possible value for m is 2, so n < L / 8.

def solution():
    BOUND = 1_500_000
    triangles = [0] * (BOUND + 1)
    for n in range(1, math.ceil(BOUND / 8)):
        for m in range(n + 1, math.ceil(BOUND / (4 * n)), 2):
            if math.gcd(m, n) == 1:
                for k in itertools.count(1):
                    a = k * (m**2 - n**2)
                    b = k * 2 * m * n
                    c = k * (m**2 + n**2)
                    L = a + b + c
                    if L <= BOUND:
                        triangles[L] += 1
                    else:
                        break
    return triangles.count(1)

print(f"{solution():,}")