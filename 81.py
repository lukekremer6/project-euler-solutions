def solution():
    with open("0081_matrix.txt") as f:
        matrix = [
            [int(num) for num in line.split(",")]
            for line in f.readlines()
        ]

        m = len(matrix)

        for i in range(m - 2, -1, -1):
            matrix[-1][i] += matrix[-1][i + 1]
            matrix[i][-1] += matrix[i + 1][-1]

        for i in range(m - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])

        return matrix[0][0]

print(f"{solution():,}")