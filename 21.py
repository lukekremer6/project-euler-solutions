def solution():
    BOUND = 10_000
    divisor_sums = [0] * BOUND
    for i in range(1, BOUND):
        j = i * 2
        while j < BOUND:
            divisor_sums[j] += i
            j += i

    return sum(
        i + j
        for i in range(BOUND)
        for j in range(i + 1, BOUND)
        if divisor_sums[i] == j and divisor_sums[j] == i
    )

print(f"{solution():,}")