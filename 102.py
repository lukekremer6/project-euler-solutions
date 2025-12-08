# For each triangle, draw lines connecting the three points.
# There are two situations where the triangle contains the origin:
#
# 1. One line passes through the origin.
# 2. At least one line crosses the y-axis below the origin,
#    and at least one line crosses the y-axis above the origin.
#
# Otherwise, the triangle does not contain the origin.

import itertools

def load_data():
    with open("0102_triangles.txt") as f:
        return [
            [
                (int(x), int(y))
                for x, y in itertools.batched(line.split(","), 2)
            ]
            for line in f.readlines()
        ]

def y_intercept(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    return y1 - m * x1

def contains_origin(triangle):
    line_positions = []
    for (x1, y1), (x2, y2) in itertools.combinations(triangle, 2):
        if x1 <= 0 <= x2 or x2 <= 0 <= x1:
            b = y_intercept(x1, y1, x2, y2)
            if x1 == x2 or b == 0:
                return True
            if b < 0:
                line_positions.append(-1)
            if b > 0:
                line_positions.append(1)
        else:
            line_positions.append(0)

    return 1 in line_positions and -1 in line_positions

def solution():
    data = load_data()
    return sum(1 for triangle in data if contains_origin(triangle))

print(f"{solution():,}")