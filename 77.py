import euler
import itertools
import functools

BOUND = 10_000
PRIMES = euler.list_primes(BOUND)
IS_PRIME = euler.list_primality(BOUND)

@functools.cache
def num_ways(n, min_additive_index):
    if n == 0:
        return 1
    return sum(
        num_ways(n - PRIMES[i], i)
        for i in itertools.takewhile(
            lambda i: PRIMES[i] <= n,
            itertools.count(min_additive_index)
        )
    )

def more_than_5000(n):
    return num_ways(n, 0) - (1 if IS_PRIME[n] else 0) > 5000

def solution():
    return next(filter(
        more_than_5000,
        itertools.count(2)
    ))

print(f"{solution():,}")