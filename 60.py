import euler
import functools
import math
import itertools

def solution():
    print("Generating primes...")
    BOUND = 100_000
    PRIMES = euler.list_primes(BOUND)
    IS_PRIME = euler.list_primality(BOUND)
    GROUP_SIZE = 5
    print("Done")

    def is_prime(n):
        if n < BOUND:
            return IS_PRIME[n]
        end = math.isqrt(n) + 1
        if any(n % p == 0
            for p in itertools.takewhile(lambda p: p <= end, PRIMES)):
            return False
        return all(
            n % i != 0
            for i in range(BOUND + 1, end)
        )

    @functools.cache
    def can_concatenate_helper(x, y):
        return is_prime(int(str(x) + str(y)))

    def can_concatenate(group, new_num):
        return all(
            can_concatenate_helper(num, new_num)
            and can_concatenate_helper(new_num, num)
            for num in group
        )

    def get_sum(target, start_position, group):
        if len(group) == GROUP_SIZE:
            return sum(group) if target > 0 else None
        else:
            for i in range(start_position, target):
                trajectory = sum(PRIMES[i : i + GROUP_SIZE - len(group)])
                if trajectory > target:
                    break
                new_num = PRIMES[i]
                if can_concatenate(group, new_num):
                    group.append(new_num)
                    candidate = get_sum(target - new_num, start_position + 1, group)
                    if candidate is not None:
                        return candidate
                    group.pop()
        return None

    target = BOUND
    while True:
        print(f"Target: {target:,}")
        lowest_sum = get_sum(target, 1, [])
        if lowest_sum is None:
            return target
        target = lowest_sum

print(f"Answer: {solution():,}")