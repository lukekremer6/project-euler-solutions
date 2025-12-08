import itertools

def num_rectangles(m, n):
    return (m + 1) * m * (n + 1) * n // 4

def solution():
    TARGET = 2_000_000
    closest = (1, 1)
    closest_distance = float("inf")

    for rows in itertools.count(1):
        for columns in itertools.count(rows):
            rectangles = num_rectangles(rows, columns)
            distance = abs(rectangles - TARGET)

            if distance < closest_distance:
                closest_distance = distance
                closest = (rows, columns)

            if rectangles > TARGET:
                break

        if num_rectangles(rows, rows) > TARGET:
            break

    return closest[0] * closest[1]

print(f"{solution():,}")