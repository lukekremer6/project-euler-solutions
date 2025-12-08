from collections import Counter
import euler

def is_pan_digital(n):
    s = str(n)
    pandigital = Counter(str(i) for i in range(1, len(s) + 1))
    return Counter(s) == pandigital

def solution():
    BOUND = 10_000_000
    primes = euler.list_primes(BOUND)
    return max(prime for prime in primes if is_pan_digital(prime))

print(f"{solution():,}")