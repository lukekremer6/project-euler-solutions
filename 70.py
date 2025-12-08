import euler
from collections import Counter

def is_permutation(n, phi):
    return Counter(str(n)) == Counter(str(phi))

def solution():
    BOUND = 10**7
    TOTIENTS = euler.list_totients(BOUND - 1)
    return min(
        (n for n in range(2, BOUND) if is_permutation(n, TOTIENTS[n])),
        key=lambda n: n / TOTIENTS[n]
    )

print(f"{solution():,}")