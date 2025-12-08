import euler

def solution():
    return sum(euler.list_totients(1_000_000)[2:])

print(f"{solution():,}")