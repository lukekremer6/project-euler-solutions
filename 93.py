import itertools
from fractions import Fraction

def op(m, n, operator):
    if operator == "+":
        return m + n
    if operator == "-":
        return m - n
    if operator == "*":
        return m * n
    if operator == "/":
        if n == 0 or n == float("inf") or m == float("inf"):
            return float("inf")
        else:
            return Fraction(m, n)
    raise ValueError

def consecutive_integers(nums):
    targets = set()
    operators = "+-*/"
    for op1, op2, op3 in itertools.product(operators, repeat=3):
        for w, x, y, z in itertools.permutations(nums):
            targets.add(op(op(op(w, x, op1), y, op2), z, op3))
            targets.add(op(op(w, op(x, y, op2), op1), z, op3))
            targets.add(op(w, op(op(x, y, op2), z, op3), op1))
            targets.add(op(w, op(x, op(y, z, op3), op2), op1))
            targets.add(op(op(w, x, op1), op(y, z, op3), op2))

    for i in itertools.count(1):
        if i not in targets:
            return i - 1

def solution():
    result = max(
        (
            (a, b, c, d)
            for a in range(1, 10)
            for b in range(a + 1, 10)
            for c in range(b + 1, 10)
            for d in range(c + 1, 10)
        ),
        key=consecutive_integers
    )

    return "".join(str(digit) for digit in result)

print(solution())