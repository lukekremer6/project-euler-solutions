import itertools
import math

def euclid_formula(m, n, k=1):
    a = k * (m**2 - n**2)
    b = k * (2 * m * n)
    c = k * (m**2 + n**2)
    return a, b, c

def out_of_bounds(a, b, M):
    return (
        a > 2 * M
        or b > 2 * M
        or a > M and b > M
    )

# Generate a list of Pythagorean triples (a, b, c)
# such that a < b < c and a <= M.
def generate_triples(M):
    triples = []
    for n in itertools.count(1):
        for m in itertools.count(n + 1, 2):
            if math.gcd(m, n) == 1:
                for k in itertools.count(1):
                    a, b, c = euclid_formula(m, n, k)
                    if out_of_bounds(a, b, M):
                        break
                    else:
                        triples.append(tuple(sorted((a, b, c))))
                a, b, c = euclid_formula(m, n)
                if out_of_bounds(a, b, M):
                    break
        a, b, c = euclid_formula(n + 1, n)
        if out_of_bounds(a, b, M):
            break
    return triples

# Given a list of Pythagorean triples, return a list of cuboids.
# All cuboids are guaranteed to have a shortest path of integer length.
# There will be no duplicate cuboids.
# For example, we can use the triple (3, 4, 5)
# to generate cuboids of dimensions 1x2x4, 1x3x3, and 2x2x3.
# All three of these cuboids have a shortest path of length 5.
def generate_cuboids(triples, M):
    cuboids = []
    for triple in triples:
        a = triple[0]
        b = triple[1]

        # The start and end parameters guarantee that width <= length <= height.
        # This means the shortest path of the cuboid is guaranteed to have length c,
        # where c is the third number in each Pythagorean triple.

        if b <= M:
            # Try partitioning a into 2 pieces.
            # No need to run this code if b > M since
            # we are forced to partition b instead.
            height = b
            start = min(a - 1, M, height)
            end = (a - 1) // 2
            for length in range(start, end, -1):
                width = a - length
                cuboids.append((width, length, height))
        
        # Try partitioning b into 2 pieces.
        height = a
        start = min(b - 1, M, height)
        end = (b - 1) // 2
        for length in range(start, end, -1):
            width = b - length
            cuboids.append((width, length, height))

    return cuboids

def find_num_solutions(M):
    triples = generate_triples(M)
    cuboids = generate_cuboids(triples, M)
    return len(cuboids)

# Do a binary search to find the first value of M
# where the number of solutions exceeds 1,000,000.
def solution():
    TARGET = 1_000_000

    M = 1

    while find_num_solutions(M) <= TARGET:
        M *= 2

    left = M // 2
    right = M
    while left < right:
        middle = (left + right) // 2
        if find_num_solutions(middle) <= TARGET:
            left = middle + 1
        else:
            right = middle
    return left

print(solution())