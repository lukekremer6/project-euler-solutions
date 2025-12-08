import math

# List whether each number is prime up to and including n
def list_primality(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False
    return primes

# List primes up to and including n
def list_primes(n):
    return [num for num, is_prime in enumerate(list_primality(n)) if is_prime]

# Check if an integer n is prime
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, math.isqrt(n) + 1))

# Check whether a nonnegative int n is a perfect square
def is_square(n):
    return n == math.isqrt(n)**2

# Calculate Euler's totient function for n given its prime factors
def totient(n, factors):
    return round(n * math.prod(1 - 1 / factor for factor in factors))

# List the totients of all numbers up to and including n
def list_totients(n):
    PRIMES = list_primes(n)
    prime_factors = [[] for _ in range(n + 1)]
    for prime in PRIMES:
        for i in range(prime, n + 1, prime):
            prime_factors[i].append(prime)
    return [totient(i, prime_factors[i]) for i in range(n + 1)]

# Calculate the digital sum of an integer n
def digital_sum(n):
    return sum(int(digit) for digit in str(n))

# Check if the integer n contains each digit from 1-9 exactly once
def is_pandigital_1_to_9(n):
    count = [0] * 10
    while n > 0:
        count[n % 10] += 1
        n //= 10
    return all(frequency == 1 for frequency in count[1:])

# Check if the integer n contains each digit from 0-9 exactly once
def is_pandigital_0_to_9(n):
    count = [0] * 10
    while n > 0:
        count[n % 10] += 1
        n //= 10
    return all(frequency == 1 for frequency in count)