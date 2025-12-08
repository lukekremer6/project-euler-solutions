import math
import functools

def solution():
    @functools.cache
    def get_factors(n):
        factors = [i for i in range(2, math.isqrt(n) + 1) if n % i == 0]
        factors += [n // factor for factor in factors] + [n]
        return factors

    def factorize(n, max_factor, partial_list):
        if n == 1:
            product = math.prod(partial_list)
            total = sum(partial_list)
            if total <= product:
                ones = product - total
                k = len(partial_list) + ones
                if 2 <= k <= BOUND:
                    min_sum_product[k] = min(min_sum_product[k], product)
        else:
            for factor in get_factors(n):
                if factor <= max_factor:
                    partial_list.append(factor)
                    factorize(n // factor, factor, partial_list)
                    partial_list.pop()

    BOUND = 12_000
    min_sum_product = [float("inf")] * (BOUND + 1)
    for i in range(2, BOUND * 2 + 1):
        factorize(i, i, [])
    return sum(set(min_sum_product[2:]))

print(f"{solution():,}")