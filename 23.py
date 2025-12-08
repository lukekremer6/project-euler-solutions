def solution():
    BOUND = 28_123
    divisor_sums = [0] * BOUND
    for i in range(1, BOUND):
        for j in range(i * 2, BOUND, i):
            divisor_sums[j] += i

    abundant_numbers = [i for i, divisor_sum in enumerate(divisor_sums) if divisor_sum > i]
    n = len(abundant_numbers)
    x = set()

    for i in range(n):
        for j in range(i, n):
            x.add(abundant_numbers[i] + abundant_numbers[j])

    y = {i for i in range(1, BOUND)}
    return sum(y - x)

print(f"{solution():,}")