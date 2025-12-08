def compress(line):
    return line.replace("C" * 9, "CM") \
                .replace("DCCCC", "CM") \
                .replace("C" * 5, "D") \
                .replace("C" * 4, "CD") \
                .replace("X" * 9, "XC") \
                .replace("LXXXX", "XC") \
                .replace("X" * 5, "L") \
                .replace("X" * 4, "XL") \
                .replace("I" * 9, "IX") \
                .replace("VIIII", "IX") \
                .replace("I" * 5, "V") \
                .replace("I" * 4, "IV")

def solution():
    with open("0089_roman.txt") as f:
        return sum(
            len(line) - len(compress(line))
            for line in f.readlines()
        )

print(solution())