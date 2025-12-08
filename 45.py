import itertools

def triangle_formula(n):
    return n * (n + 1) // 2

def pentagonal_formula(n):
    return n * (3 * n - 1) // 2

def hexagonal_formula(n):
    return n * (2 * n - 1)

def solution():
    i = 286
    j = 166
    k = 144

    while True:
        triangle = triangle_formula(i)
        pentagon = pentagonal_formula(j)
        hexagon = hexagonal_formula(k)

        if triangle == pentagon == hexagon:
            return triangle
        elif pentagon < triangle:
            j += 1
        elif hexagon < triangle:
            k += 1
        else:
            i += 1

print(f"{solution():,}")