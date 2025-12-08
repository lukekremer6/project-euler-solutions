import euler

def solution():
    BOUND = 1_000_001
    TOTIENTS = euler.list_totients(BOUND)
    return max(range(2, BOUND), key=lambda n: n / TOTIENTS[n])

print(solution())