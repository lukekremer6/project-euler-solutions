import csv

def to_num(char):
    return ord(char) - ord("A") + 1

def alphabetical_value(name):
    return sum(to_num(char) for char in name)

def solution():
    with open("0022_names.txt") as f:
        csv_reader = csv.reader(f)
        names = [name for row in csv_reader for name in row]
        names.sort()
        return sum(alphabetical_value(name) * (i + 1) for i, name in enumerate(names))

print(f"{solution():,}")