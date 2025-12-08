import math

def solution(n):
    triangle_number = 0
    i = 1

    while True:
        triangle_number += i
        sq = math.isqrt(triangle_number)
        num_factors = sum(2 for j in range(1, sq) if triangle_number % j == 0)

        if triangle_number % sq == 0:
            num_factors += 1

        if num_factors > n:
            return triangle_number

        i += 1

print(f"{solution(500):,}")