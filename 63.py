import itertools

# Let a * 10**(n - 1) = b**n, where 1 < a < 10 and b > 0 is an integer.
# If b >= 10, then b**n will always be larger and equality is impossible.
# So 0 < b < 10.
#
# At some point, 10**(n - 1) will become larger than 9**n,
# so we can use that point as an upper bound.

def solution():
    upper_bound = next(filter(
        lambda n: 10**(n - 1) > 9**n,
        itertools.count()
    ))

    return sum(
        1 for n in range(1, upper_bound)
        for b in range(1, 10)
        if len(str(b**n)) == n
    )

print(f"{solution():,}")