import functools

# Use recursion to find the number of ways to add up n.
# max_additive ensures that we only add numbers in descending order
# to avoid duplicates. For example, suppose n is 5 and max_additive is 2.
# Then we will not consider any sequences with numbers greater than 2.
# Instead, we will only consider the sequences 2 + 2 + 1,
# 2 + 1 + 1 + 1, and 1 + 1 + 1 + 1 + 1.

@functools.cache
def num_ways(n, max_additive):
    if n == 0:
        return 1
    return sum(
        num_ways(n - i, i)
        for i in range(min(max_additive, n), 0, -1)
    )

def solution():
    TARGET = 100
    return num_ways(TARGET, TARGET - 1)

print(f"{solution():,}")