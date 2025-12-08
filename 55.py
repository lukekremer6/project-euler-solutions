def is_palindrome(num):
    return str(num) == str(num)[::-1]

def get_reverse(num):
    return int(str(num)[::-1])

def is_lychrel(num):
    for _ in range(50):
        num += get_reverse(num)
        if is_palindrome(num):
            return False
    return True

def solution():
    return sum(1 for i in range(10_000) if is_lychrel(i))

print(solution())