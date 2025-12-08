import math

def solution(n):
    return math.comb(n * 2, n)

print(f"{solution(20):,}")