import euler

def solution():
    TARGET = 8
    BOUND = 1_000_000
    PRIMES = euler.list_primality(BOUND)
    for i in range(BOUND):
        if PRIMES[i]:
            for old_digit in range(10):
                string = str(i)
                if str(old_digit) in string:
                    count = sum(
                        1 for new_digit in range(1 if string[0] == str(old_digit) else 0, 10)
                        if PRIMES[int(str(i).replace(str(old_digit), str(new_digit)))]
                    )
                    if count == TARGET:
                        return i
    raise AssertionError("NOT FOUND")

print(solution())