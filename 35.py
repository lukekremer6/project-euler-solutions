import euler

primes = euler.list_primality(1_000_000)

def is_circular_prime(n):
    rotation = n
    digits = len(str(n))
    for _ in range(digits):
        if not primes[rotation]:
            return False
        lastDigit = rotation % 10
        rotation //= 10
        rotation += lastDigit * 10**(digits - 1)
    return True

def solution():
    return sum(1 for i in range(1_000_000) if is_circular_prime(i))

print(f"{solution():,}")