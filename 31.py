import functools

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def solution():

    @functools.cache
    def helper(target, i):
        if target == 0:
            return 1
        if target < 0 or i >= len(coins):
            return 0
        return helper(target - coins[i], i) + helper(target, i + 1)

    return helper(200, 0)

print(f"{solution():,}")