from fractions import Fraction
import math

def solution():
    BOUND = 1_000_000
    TARGET = Fraction(3, 7)
    return max(
        Fraction(
            TARGET * d - 1
            if d % TARGET.denominator == 0
            else math.floor(TARGET * d),
            d
        )
        for d in range(2, BOUND + 1)
    ).numerator

print(f"{solution():,}")