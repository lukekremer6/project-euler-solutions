import itertools

def has_property(number):
    primes = [1, 2, 3, 5, 7, 11, 13, 17]
    return all(
        int("".join(number[i : i + 3])) % primes[i] == 0
        for i in range(1, 8)
    )

def solution():
    pandigital_numbers = itertools.permutations("0123456789")
    return sum(
        int("".join(number)) for number in pandigital_numbers
        if has_property(number) and number[0] != "0"
    )

print(f"{solution():,}")