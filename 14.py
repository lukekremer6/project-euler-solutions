import functools

@functools.cache
def collatz_sequence(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz_sequence(n // 2)
    else:
        return 1 + collatz_sequence(n * 3 + 1)

def solution(x):
    return max(range(1, x), key=collatz_sequence)

print(solution(1_000_000))