def solution():
    return sum(int(digit) for digit in str(2**1000))

print(f"{solution():,}")