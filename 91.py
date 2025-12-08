from fractions import Fraction

def is_perpendicular(slope1, slope2):
    if slope2 == float("inf"):
        return slope1 == 0
    elif slope2 == 0:
        return slope1 == float("inf")
    else:
        return slope1 == Fraction(-1, slope2)

def slope(x1, y1, x2, y2):
    return Fraction(y2 - y1, x2 - x1) if x2 - x1 != 0 else float("inf")

def is_right_triangle(Ox, Oy, Px, Py, Qx, Qy):
    # Calculate the slope of each line.
    # If any two lines are perpendicular, then the three points
    # form a right triangle.

    slope_PQ = slope(Px, Py, Qx, Qy)
    slope_OP = slope(Ox, Oy, Px, Py)
    slope_OQ = slope(Ox, Oy, Qx, Qy)

    return (
        is_perpendicular(slope_PQ, slope_OP)
        or is_perpendicular(slope_OP, slope_OQ)
        or is_perpendicular(slope_OQ, slope_PQ)
    )

def solution():
    BOUND = 50
    Ox = 0
    Oy = 0

    return sum(
        1
        for Px in range(BOUND + 1)
        for Py in range(1 if Px == Ox else 0, BOUND + 1)
        for Qx in range(Px, BOUND + 1)
        for Qy in range(Py + 1 if Qx == Px else 0, BOUND + 1)
        if is_right_triangle(Ox, Oy, Px, Py, Qx, Qy)
    )

print(f"{solution():,}")