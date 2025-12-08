def solution():
    numerator = 3
    denominator = 2
    count = 0
    for _ in range(1000):
        if len(str(numerator)) > len(str(denominator)):
            count += 1
        numerator, denominator = numerator + denominator * 2, numerator + denominator
    return count

print(solution())