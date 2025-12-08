from collections import Counter

pandigital = Counter(str(i) for i in range(1, 10))

def is_pandigital(s):
    return Counter(s) == pandigital

def solution():
    result = "0"
    for i in range(1, 10_000):
        num = ""
        n = 1
        while len(num) < 9:
            num += str(i * n)
            n += 1
        if is_pandigital(num):
            result = max(result, num)
    return result

print(solution())