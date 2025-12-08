import euler

def solution():
    primes = euler.list_primes(1_000_000)
    return primes[10_001]

print(f"{solution():,}")