def find_multiples(a, b, n):
    multiples_a = {i for i in range(a, n, a)}
    multiples_b = {i for i in range(b, n, b)}
    multiples_a_or_b = multiples_a | multiples_b
    return sum(multiples_a_or_b)

print(f"{find_multiples(3, 5, 1000):,}")