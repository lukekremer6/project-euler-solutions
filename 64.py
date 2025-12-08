import math
import itertools
import euler

def get_period(n):
    # To find the period, we start with a fraction, such as
    # 1 / (sqrt(23) - 4). Then we repeat the following steps:
    #
    # 1. Find the conjugate of the denominator and multiply
    #    our current fraction by this conjugate.
    #
    #       For example, if we start with 1 / (sqrt(23) - 4),
    #       then the denominator's conjugate is sqrt(23) + 4.
    #       So we multiply our fraciton by (sqrt(23) + 4) / (sqrt(23) + 4)
    #       and simplify to get (sqrt(23) + 4) / 7.
    #
    # 2. Find the value of a by evaluating our original
    #    fraction and truncating it.
    #
    #       For example, if our fraction is 1 / (sqrt(23) - 4),
    #       then this evaluates to ~1.256 and we truncate it to 1.
    #
    # 3. Subtract a from the simplified fraction we created in step 1.
    #
    #       For example, if our simplified fraction is
    #       (sqrt(23) + 4) / 7, then we subtract a and get
    #       (sqrt(23) - 3) / 7.
    #
    # 4. Invert our fraction from step 3.
    #
    #       For example, if we start with (sqrt(23) - 3) / 7,
    #       then we get 7 / (sqrt(23) - 3).
    #
    # 5. Use our fraction from step 4 as our new fraction
    #    for the next iteration. Repeat the process until we end up back
    #    where we started.
    #
    # a, b, c, d, e, and n represent the constants in these equations:
    # b / (sqrt(n) - c) == (sqrt(n) + c) / d == a + (sqrt(n) - e) / d
    # 
    # For example, if n = 23, b = 1, c = 4, d = 7, e = 3, and a == 1, then we have
    # 1 / (sqrt(23) - 4) == (sqrt(23) + 4) / 7 == 1 + (sqrt(23) - 3) / 7

    seen = {}
    b = 1
    c = math.isqrt(n)
    for i in itertools.count():
        if (b, c) in seen:
            return i - seen[(b, c)]
        seen[(b, c)] = i

        # Multiply our fraction by the denominator's
        # conjugate and simplify
        d = (n - c**2) // b

        # Find a
        a = math.trunc(b / (math.sqrt(n) - c))

        # Subtract a from our simplified fraction
        e = d * a - c

        # Prepare for next iteration
        b = d
        c = e

def solution():
    return sum(
        1 for n in range(2, 10_001)
        if not euler.is_square(n)
        and get_period(n) % 2 == 1
    )

print(solution())