import euler

def solution():
    UPPER_BOUND = 1_000_000
    IS_PRIME = euler.list_primality(UPPER_BOUND)
    PRIMES = euler.list_primes(UPPER_BOUND)
    result = -1
    max_length = 0
    for i in range(len(PRIMES)):
        total = 0
        for j in range(i, len(PRIMES)):
            total += PRIMES[j]
            if total < UPPER_BOUND:
                current_length = j - i - 1
                if IS_PRIME[total] and current_length > max_length:
                    max_length = current_length
                    result = total
            else:
                break
    return result

print(f"{solution():,}")