# test matrix
# matrix = [
#     [131, 673, 234, 103, 18],
#     [201, 96, 342, 965, 150],
#     [630, 803, 746, 422, 111],
#     [537, 699, 497, 121, 956],
#     [805, 732, 524, 37, 331]
# ]

from collections import deque

# Similar to Dijkstra's algorithm.
# Use breadth-first search to find the shortest path from
# the top left to all the other cells.
def solution():
    with open("0083_matrix.txt") as f:
        matrix = [
            [int(num) for num in line.split(",")]
            for line in f.readlines()
        ]

        n = len(matrix)
        q = deque()
        q.append((0, 0, 0))
        dp = [[float("inf")] * n for _ in range(n)]

        while q:
            i, j, value = q.popleft()
            if 0 <= i < n and 0 <= j < n:
                new_value = matrix[i][j] + value
                if new_value < dp[i][j]:
                    dp[i][j] = new_value
                    directions = ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1))
                    for i_dir, j_dir in directions:
                        q.append((i_dir, j_dir, new_value))

        return dp[-1][-1]

print(f"{solution():,}")