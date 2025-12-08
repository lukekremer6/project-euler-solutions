import euler

def solution():
    primes = euler.list_primes(2_000_000)
    return sum(primes)

print(f"{solution():,}")