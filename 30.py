# All numbers should be 6 digits or less

def sum_of_fifth_powers(n):
    s = str(n)
    return n == sum(int(digit)**5 for digit in s)

def solution():
    return sum(i for i in range(2, 1_000_000) if sum_of_fifth_powers(i))

print(f"{solution():,}")