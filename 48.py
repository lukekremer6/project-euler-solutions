def solution():
    n = 1000
    MOD = 10**10
    return sum(pow(i, i, MOD) for i in range(1, n + 1)) % MOD

print(f"{solution():,}")