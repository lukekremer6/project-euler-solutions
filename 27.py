import itertools
import math
import euler

def formula(a, b, n):
    return n**2 + a * n + b

primes = euler.list_primality(10_000)

def is_prime(n):
    if n < 0:
        return False
    if n < len(primes):
        return primes[n]
    return euler.is_prime(n)

def count_primes(ab):
    a, b = ab
    for n in itertools.count():
        y = formula(a, b, n)
        if not is_prime(y):
            return n

def solution():
    return math.prod(
        max(
            (
                (a, b)
                for a in range(-999, 1000)
                for b in range(-1000, 1001)
            ),
            key=count_primes
        )
    )

print(f"{solution():,}")