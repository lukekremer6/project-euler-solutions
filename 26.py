import itertools

def find_repetend_len(denominator):
    numerator = 1
    seen = {}
    for i in itertools.count():
        if numerator in seen:
            return i - seen[numerator]
        seen[numerator] = i
        numerator = numerator * 10 % denominator

def solution():
    return max(range(2, 1000), key=find_repetend_len)

print(solution())