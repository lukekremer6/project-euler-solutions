import itertools
import math

def find_blue_discs(total):
    return 0.5 + math.sqrt(0.5 * total * (total - 1) + 0.25)

def equation(b, t):
    return 2 * b * (b - 1) == t * (t - 1)

def solution():
    arrangements = []
    for t in itertools.count(2):
        b = math.floor(find_blue_discs(t))
        if equation(b, t):
            arrangements.append((b, t))
            if len(arrangements) > 2:
                break

    while True:
        start = arrangements[-1][1]**2 // arrangements[-2][1]
        for t in itertools.count(start):
            b = math.floor(find_blue_discs(t))
            if equation(b, t):
                arrangements.append((b, t))
                if t > 10**12:
                    return b
                break

print(f"{solution():,}")