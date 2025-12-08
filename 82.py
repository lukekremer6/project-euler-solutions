# test matrix
# matrix = [
#     [131, 673, 234, 103, 18],
#     [201, 96, 342, 965, 150],
#     [630, 803, 746, 422, 111],
#     [537, 699, 497, 121, 956],
#     [805, 732, 524, 37, 331]
# ]

def solution():
    with open("0082_matrix.txt") as f:
        matrix = [
            [int(num) for num in line.split(",")]
            for line in f.readlines()
        ]

        n = len(matrix)
        for j in range(n - 2, -1, -1):
            # Try going up or right
            column_up = [matrix[i][j] for i in range(n)]
            column_up[0] += matrix[0][j + 1]
            for i in range(1, n):
                column_up[i] += min(matrix[i][j + 1], column_up[i - 1])

            # Try going down or right
            column_down = [matrix[i][j] for i in range(n)]
            column_down[-1] += matrix[-1][j + 1]
            for i in range(n - 2, -1, -1):
                column_down[i] += min(matrix[i][j + 1], column_down[i + 1])

            # Try going up, down, or right
            for i in range(n):
                matrix[i][j] = min(column_up[i], column_down[i])

        return min(matrix[i][0] for i in range(n))

print(f"{solution():,}")