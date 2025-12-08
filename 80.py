import decimal
import euler

def digital_sum(n, NUM_DIGITS):
    return sum(int(digit) for digit in str(n).replace(".", "")[:NUM_DIGITS])

def solution():
    NUM_DIGITS = 100
    BOUND = 100
    decimal.getcontext().prec = NUM_DIGITS + 2
    return sum(
        digital_sum(decimal.Decimal(n).sqrt(), NUM_DIGITS)
        for n in range(BOUND)
        if not euler.is_square(n)
    )

print(f"{solution():,}")