import itertools

SQUARES = {str(i**2).zfill(2) for i in range(1, 10)}

def duplicate69(cube):
    if "6" in cube and "9" not in cube:
        return cube + ("9",)
    if "9" in cube and "6" not in cube:
        return cube + ("6",)
    return cube

def can_make_all_squares(cube1, cube2):
    can_make_squares = {square: False for square in SQUARES}

    pairs = itertools.chain(
        itertools.product(cube1, cube2),
        itertools.product(cube2, cube1)
    )

    for pair in pairs:
        s = "".join(pair)
        if s in can_make_squares:
            can_make_squares[s] = True

    return all(can_make_squares.values())

def solution():
    DIGITS = tuple(str(num) for num in range(10))

    # We need to divide by 2 because the cubes are indistinguishable
    # and we want to eliminate duplicates.
    return sum(
        1
        for cube1 in itertools.combinations(DIGITS, 6)
        for cube2 in itertools.combinations(DIGITS, 6)
        if can_make_all_squares(duplicate69(cube1), duplicate69(cube2))
    ) // 2

print(solution())