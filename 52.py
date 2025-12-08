from collections import Counter
import itertools

def solution():
    for x in itertools.count(1):
        if all(Counter(str(x)) == Counter(str(x * i)) for i in range(2, 7)):
            return x

print(f"{solution():,}")