import itertools

def solution():
    digits = range(10)
    target = 999_999
    p = itertools.permutations(digits)
    x = itertools.islice(p, target, None)
    return "".join(str(i) for i in next(x))

print(solution())