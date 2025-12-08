def load_nums():
    with open("0099_base_exp.txt") as f:
        return [
            [int(num) for num in line.split(",")]
            for line in f.readlines()
        ]

def solution():
    nums = load_nums()
    calc = lambda i: nums[i][0]**(nums[i][1] / 100_000)
    return max(range(1000), key=calc) + 1

print(solution())