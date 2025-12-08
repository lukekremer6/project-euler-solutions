import functools

# Top down solution
def solution():
    @functools.cache
    def helper(i, j):
        if i == n:
            return 0
        return triangle[i][j] + max(helper(i + 1, j), helper(i + 1, j + 1))

    with open("0067_triangle.txt") as f:
        triangle = [
            [int(num) for num in line.rstrip().split(" ")]
            for line in f.readlines()
        ]
        n = len(triangle)
        return helper(0, 0)

# Bottom up solution
def solution2():
    with open("0067_triangle.txt") as f:
        triangle = [
            [int(num) for num in line.rstrip().split(" ")]
            for line in f.readlines()
        ]
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

print(f"{solution2():,}")