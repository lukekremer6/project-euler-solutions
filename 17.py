def length_of_num(n):
    ones = {
        1: 3,
        2: 3,
        3: 5,
        4: 4,
        5: 4,
        6: 3,
        7: 5,
        8: 5,
        9: 4
    }

    tens = {
        2: 6,
        3: 6,
        4: 5,
        5: 5,
        6: 5,
        7: 7,
        8: 6,
        9: 6
    }

    teens = {
        10: 3,
        11: 6,
        12: 6,
        13: 8,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 8,
        19: 8
    }

    result = 0
    if n == 1000:
        return 11

    and_flag = False

    hundreds_place = n // 100
    if hundreds_place > 0:
        result += ones[hundreds_place] + 7
    
    n %= 100
    tens_place = n // 10
    if tens_place > 0 and hundreds_place > 0:
        and_flag = True
    if tens_place > 1:
        result += tens[tens_place]

    if tens_place == 1:
        result += teens[n]
    else:
        n %= 10
        ones_place = n
        if ones_place > 0 and hundreds_place > 0:
            and_flag = True
        if ones_place > 0:
            result += ones[ones_place]

    if and_flag:
        result += 3

    return result

def solution():
    return sum(length_of_num(i) for i in range(1, 1001))

print(f"{solution():,}")