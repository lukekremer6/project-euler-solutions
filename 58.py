import itertools
import euler

def solution():
    num_primes = 0
    num_numbers = 1
    for i in itertools.count(3, 2):
        corners = [i**2 - (i - 1) * j for j in range(1, 4)]
        num_primes += sum(1 for corner in corners if euler.is_prime(corner))
        num_numbers += 4
        if num_primes / num_numbers < 0.1:
            return i

print(f"{solution():,}")