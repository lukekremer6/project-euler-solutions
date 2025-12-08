def is_palindrome(s):
    return s == s[::-1]

def solution():
    BOUND = 1_000_000
    return sum(
        i for i in range(BOUND)
        if is_palindrome(str(i)) and is_palindrome(bin(i)[2:])
    )

print(f"{solution():,}")