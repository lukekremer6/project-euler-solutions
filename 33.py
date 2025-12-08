from fractions import Fraction

def is_curious(numerator, denominator):
    n1 = numerator // 10
    n2 = numerator % 10
    s1 = denominator // 10
    s2 = denominator % 10

    return (
        n1 == s1 and numerator / denominator == n2 / s2 or
        n1 == s2 and numerator / denominator == n2 / s1 or
        n2 == s1 and numerator / denominator == n1 / s2 or
        n2 == s2 and numerator / denominator == n1 / s1
    )

def solution():
    result = 1
    for numerator in range(11, 100):
        for denominator in range(numerator + 1, 100):
            if denominator % 10 != 0 and is_curious(numerator, denominator):
                result *= Fraction(numerator, denominator)
    return result.denominator

print(solution())