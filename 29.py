def solution():
    return len({a**b for a in range(2, 101) for b in range(2, 101)})

print(solution())