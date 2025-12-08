# Check if the number at location (i, j)
# has any duplicates in its row, column, or box.
def is_valid(grid, i, j):
    num = grid[i][j]

    row = grid[i]
    column = [grid[row][j] for row in range(9)]
    box = [
        grid[row + (i // 3) * 3][column + (j // 3) * 3]
        for row in range(3)
        for column in range(3)
    ]

    return (
        row.count(num) <= 1
        and column.count(num) <= 1
        and box.count(num) <= 1
    )

# Helper function for solve_sudoku.
# If we've solved the entire puzzle, return True.
# Otherwise, try to solve the rest of the puzzle.
# If cell (i, j) is invalid or it's impossible to solve the
# rest of the puzzle, then return False.
def can_solve(grid, i, j):
    return is_valid(grid, i, j) and (
        i == 8 and j == 8
        or i < 8 and j == 8 and solve_sudoku(grid, i + 1, 0)
        or j < 8 and solve_sudoku(grid, i, j + 1)
    )

# Use trial and error to solve the puzzle.
# Return True if a correct solution is found and False if not.
def solve_sudoku(grid, i, j):
    if grid[i][j] == 0:
        for num in range(1, 10):
            grid[i][j] = num
            if can_solve(grid, i, j):
                return True
        grid[i][j] = 0
        return False

    else:
        return can_solve(grid, i, j)

# Solve the puzzle and return its 3-digit number.
def find_3_digit_number(grid):
    assert solve_sudoku(grid, 0, 0) == True
    return grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]

def load_grids():
    with open("0096_sudoku.txt") as f:
        s = f.readlines()
        num_grids = len(s) // 10
        return [
            [
                [int(digit) for digit in s[j].rstrip()]
                for j in range(i * 10 + 1, i * 10 + 10)
            ]
            for i in range(num_grids)
        ]

def solution():
    grids = load_grids()

    return sum(
        find_3_digit_number(grid)
        for grid in grids
    )

print(f"{solution():,}")