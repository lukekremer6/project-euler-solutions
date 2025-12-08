import math
import itertools
import functools

@functools.cache
def count_distinct_prime_factors(n):
    if n == 0 or n == 1:
        return 0
    count = 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            return count + count_distinct_prime_factors(n)
    return count

def solution(n):
    currentStreak = 0
    for i in itertools.count(4):
        if count_distinct_prime_factors(i) == n:
            currentStreak += 1
        else:
            currentStreak = 0
        if currentStreak == n:
            return i - n + 1

print(f"{solution(4):,}")