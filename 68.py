import itertools
import numpy as np

def solution():
    RING_SIZE = 5
    rings = set()

    for permutation in itertools.permutations(range(1, RING_SIZE * 2 + 1)):
        ring = [
            (
                permutation[i + RING_SIZE],
                permutation[i],
                permutation[(i + 1) % RING_SIZE]
            )
            for i in range(RING_SIZE)
        ]

        # Check if all lines have the same sum
        line_sum = sum(ring[0])
        if all(line_sum == sum(ring[i]) for i in range(1, RING_SIZE)):

            # Find line with lowest external node
            start = np.argmin([line[0] for line in ring])

            # Go clockwise
            group = tuple(
                itertools.islice(
                    itertools.cycle(ring),
                    start,
                    start + RING_SIZE
                )
            )

            rings.add(group)

    strings = [
        "".join(
            str(num)
            for num in itertools.chain.from_iterable(ring)
        )
        for ring in rings
    ]

    return max(int(string) for string in strings if len(string) == 16)

print(f"{solution():,}")