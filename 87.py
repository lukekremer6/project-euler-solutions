import euler
import math

def sum_of_exponents(i, j, k):
    return i**2 + j**3 + k**4

def solution():
    BOUND = 50_000_000
    PRIMES = euler.list_primes(math.isqrt(BOUND))
    dp = [False] * BOUND
    for i in PRIMES:
        if sum_of_exponents(i, 2, 2) >= BOUND:
            break
        for j in PRIMES:
            if sum_of_exponents(i, j, 2) >= BOUND:
                break
            for k in PRIMES:
                total = sum_of_exponents(i, j, k)
                if total >= BOUND:
                    break
                dp[total] = True
    return dp.count(True)

print(f"{solution():,}")