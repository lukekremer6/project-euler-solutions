import itertools

def triangle(n):
    return n * (n + 1) // 2

def square(n):
    return n**2

def pentagonal(n):
    return n * (3 * n - 1) // 2

def hexagonal(n):
    return n * (2 * n - 1)

def heptagonal(n):
    return n * (5 * n - 3) // 2

def octagonal(n):
    return n * (3 * n - 2)

def generate_polygonal_nums(func):
    return set(
        itertools.dropwhile(
            lambda num: num < 1000,
            itertools.takewhile(
                lambda num: num < 10_000,
                (func(n) for n in itertools.count())
            )
        )
    )

def solution():
    funcs = [
        triangle,
        square,
        pentagonal,
        hexagonal,
        heptagonal,
        octagonal
    ]

    polygonal_nums = {
        func.__name__: generate_polygonal_nums(func)
        for func in funcs
    }

    def find_sum(cycle, shapes_used):
        if len(cycle) == 6:
            if cycle[-1] % 100 == cycle[0] // 100:
                return sum(cycle)
        else:
            first_two_digits = cycle[-1] % 100
            for last_two_digits in range(10, 100):
                num = first_two_digits * 100 + last_two_digits
                for polygon, nums in polygonal_nums.items():
                    if polygon not in shapes_used and num in nums:
                        cycle.append(num)
                        shapes_used.add(polygon)
                        result = find_sum(cycle, shapes_used)
                        if result is not None:
                            return result
                        cycle.pop()
                        shapes_used.remove(polygon)
        return None

    return next(filter(
        lambda num: num is not None,
        (find_sum([triangle_num], {"triangle"})
        for triangle_num in polygonal_nums["triangle"])
    ))

print(f"{solution():,}")