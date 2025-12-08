import itertools

def create_spiral(n):

    def helper(spiral, n):
        left = (len(spiral) - n) // 2
        right = left + n
        upper = left
        lower = right

        if n == 1:
            spiral[upper][left] = 1
            return 1

        count = itertools.count(
            helper(spiral, n - 2) + 1
        )

        # Right
        for i in range(upper + 1, lower):
            spiral[i][right - 1] = next(count)
        
        # Bottom
        for j in range(right - 2, left - 1, -1):
            spiral[lower - 1][j] = next(count)
        
        # Left
        for i in range(lower - 2, upper - 1, -1):
            spiral[i][left] = next(count)
        
        # Top
        for j in range(left + 1, right):
            spiral[upper][j] = next(count)
        
        return spiral[upper][right - 1]

    spiral = [[0] * n for _ in range(n)]
    helper(spiral, n)
    return spiral

def sum_diagonals(spiral):
    n = len(spiral)
    return sum(spiral[i][i] + spiral[i][n - i - 1] for i in range(n)) - 1

def solution():
    SIZE = 1001
    return 1 + sum(4 * n**2 - 6 * n + 6 for n in range(3, SIZE + 1, 2))

print(f"{solution():,}")