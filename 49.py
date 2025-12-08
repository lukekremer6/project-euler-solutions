from collections import Counter
import euler

def has_same_digits(x, y, z):
    return Counter(str(x)) == Counter(str(y)) == Counter(str(z))

def solution():
    NUM_DIGITS = 4
    LOWER_BOUND = 10**(NUM_DIGITS - 1)
    UPPER_BOUND = 10**(NUM_DIGITS)
    IS_PRIME = euler.list_primality(UPPER_BOUND)
    for x in range(LOWER_BOUND, UPPER_BOUND):
        for step in range(1, (UPPER_BOUND - x - 1) // 2 + 1):
            y = x + step
            z = y + step
            if (IS_PRIME[x] and IS_PRIME[y] and IS_PRIME[z]
                and has_same_digits(x, y, z)
                and x != 1487 and y != 4817 and z != 8147):
                return str(x) + str(y) + str(z)
    return "FAILURE"

print(solution())