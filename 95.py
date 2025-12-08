def solution():
    BOUND = 10**6

    chain_length = [-1] * (BOUND + 1)
    min_element = [float("inf")] * (BOUND + 1)
    sum_of_proper_divisors = [0] * (BOUND + 1)

    for i in range(1, BOUND + 1):
        for j in range(i * 2, BOUND + 1, i):
            sum_of_proper_divisors[j] += i

    for i in range(BOUND + 1):
        n = i
        seen = {}
        j = 0

        while n not in seen:
            seen[n] = j
            n = sum_of_proper_divisors[n]
            j += 1

            # Out of bounds
            if n > BOUND:
                for key in seen.keys():
                    chain_length[key] = 0
                    min_element[key] = 0
                break

            # We've already seen a number in this chain
            if chain_length[n] != -1:
                for key in seen.keys():
                    chain_length[key] = chain_length[n]
                    min_element[key] = min_element[n]
                break

        else:
            current_chain_length = j - seen[n]

            # Go around the chain once to find the minimum
            minimum = n
            for _ in range(current_chain_length):
                minimum = min(minimum, n)
                n = sum_of_proper_divisors[n]

            # Go around the chain again to update
            # chain_length and min_element
            for _ in range(current_chain_length):
                chain_length[n] = current_chain_length
                min_element[n] = minimum
                n = sum_of_proper_divisors[n]
    
    longest_chain = max(range(BOUND + 1), key=lambda i: chain_length[i])
    return min_element[longest_chain]

print(solution())