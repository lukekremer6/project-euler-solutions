import math

# Solution 1
def num_solutions(p):
    return sum(
        1
        for a in range(1, p // 2)
        for b in range(a, p - a)
        if a**2 + b**2 == (p - a - b)**2
    )

def solution1():
    return max(range(1, 1001), key=num_solutions)

# Solution 2 (faster)
def euclid_formula():
    BOUND = 1001
    triples = {i: set() for i in range(3, BOUND)}
    for n in range(1, math.isqrt(BOUND) + 1):
        for m in range(n + 1, BOUND // (2 * n)):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2

            a2 = a
            b2 = b
            c2 = c

            while True:
                a2 += a
                b2 += b
                c2 += c

                triple = tuple(sorted((a2, b2, c2)))
                p = a2 + b2 + c2

                if p < BOUND:
                    triples[p].add(triple)
                else:
                    break
    return triples

def solution2():
    triples = euclid_formula()
    return max(triples, key=lambda x: len(triples[x]))

print(solution2())