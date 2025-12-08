def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

def solution(bound):
    g = fibonacci()
    result = 0
    num = next(g)
    while num < bound:
        if num % 2 == 0:
            result += num
        num = next(g)
    return result

print(f"{solution(4000000):,}")