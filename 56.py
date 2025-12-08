def digital_sum(num):
    return sum(int(digit) for digit in str(num))

def solution():
    return max(digital_sum(a**b) for a in range(100) for b in range(100))

print(solution())