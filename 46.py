import euler
import itertools
import math

def solution():
    BOUND = 10_000
    IS_PRIME = euler.list_primality(BOUND)
    for composite in itertools.count(9, 2):
        if not IS_PRIME[composite]:
            for i in range(1, math.isqrt(composite) + 1):
                if IS_PRIME[composite - 2 * i**2]:
                    break
            else:
                return composite

print(f"{solution():,}")