import math
import euler

def solution(n):
    sq = math.isqrt(n)
    primes = euler.list_primes(sq)
    factors = set()
    for p in primes:
        if p > n:
            break
        while n % p == 0:
            n //= p
            factors.add(p)
    factors.add(n)
    return max(factors)

print(f"{solution(600_851_475_143):,}")