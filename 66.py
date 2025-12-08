import euler
import itertools
import math
from fractions import Fraction

# Get the infinite sequence of numbers in the continued fraction
# representation of sqrt(n).
def get_block(n):
    seen = {}
    b = 1
    c = math.isqrt(n)
    block = []
    for i in itertools.count():
        if (b, c) in seen:
            return block
        seen[(b, c)] = i
        d = (n - c**2) // b
        a = math.trunc(b / (math.sqrt(n) - c))
        block.append(a)
        e = d * a - c
        b = d
        c = e

def continued_fraction(r, block, i, target):
    a = block[(i - 1) % r]
    if i == target:
        return Fraction(1, a)
    return Fraction(1, a + continued_fraction(r, block, i + 1, target))

def convergent(r, block, D, target):
    if target == 0:
        return math.isqrt(D)
    return math.isqrt(D) + continued_fraction(r, block, 1, target)

def find_minimal_solution(D):
    block = get_block(D)
    r = len(block)
    result = convergent(
        r,
        block,
        D,
        r - 1 if r % 2 == 0 else 2 * r - 1
    )
    return result.numerator

def solution():
    return max(
        (D for D in range(2, 1001) if not euler.is_square(D)),
        key=find_minimal_solution
    )

print(solution())