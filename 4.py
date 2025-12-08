def isPalindrome(n):
    s = str(n)
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def solution(n):
    palindromes = []
    for i in range(int("9" * n), -1, -1):
        for j in range(int("9" * n), -1, -1):
            product = i * j
            if isPalindrome(product):
                palindromes.append(product)
                break
    return max(palindromes)

print(f"{solution(3):,}")