import euler

BOUND = 1_000_000
primes = euler.list_primality(BOUND)

def is_truncatable(n):
    i = 10
    while i <= n:
        if not primes[n % i]:
            return False
        i *= 10
    while n:
        if not primes[n]:
            return False
        n //= 10
    return True

def solution():
    return sum(i for i in range(10, BOUND) if is_truncatable(i))

print(f"{solution():,}")