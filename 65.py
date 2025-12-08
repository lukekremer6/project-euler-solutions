from fractions import Fraction

def piecewise(i):
    return Fraction(2 * (i + 1), 3) if i % 3 == 2 else 1

def continued_fraction(i, target):
    return Fraction(
        1,
        piecewise(i) + (
            0 if i == target
            else continued_fraction(i + 1, target)
        )
    )

def convergent(target):
    return 2 + continued_fraction(1, target - 1)

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def solution():
    return sum_of_digits(convergent(100).numerator)

print(solution())