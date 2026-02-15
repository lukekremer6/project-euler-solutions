import itertools
from collections import defaultdict

def num_digits(num):
    return len(str(num))

def solution():
    # Maps a permutation to a list of cubes that can generate it.
    # For example, "01234566" maps to [345, 384, 405].
    permutation_to_cubes = defaultdict(list)

    cur_num_digits = 1
    for i in itertools.count(1):
        cube = i**3

        # If the number of digits in the cube increases, then it's impossible
        # for the new cube or any cubes beyond it to be a permutation of a
        # previous cube with fewer digits.
        # For example, 4**3 = 64 and 5**3 = 125. 125 has more digits than 64,
        # so 125 cannot possibly be a permutation of any previous cube.
        # Every time the number of digits increases, we review all the cubes
        # we've seen so far and check if we have exactly five permutations of
        # any of them.
        if num_digits(cube) > cur_num_digits:
            cur_num_digits = num_digits(cube)
            for nums in permutation_to_cubes.values():
                if len(nums) == 5:
                    return min(nums)**3

        key = "".join(sorted(str(cube)))
        permutation_to_cubes[key].append(i)

print(f"{solution():,}")