import itertools

def formula(n):
    return n * (3 * n - 1) // 2

def solution():
    pentagonal_numbers_set = {1, 5}
    pentagonal_numbers_list = [0, 1, 5]
    max_in_set = max(pentagonal_numbers_set)
    D = float("inf")
    for i in itertools.count(2):
        P_k = pentagonal_numbers_list[i]
        if P_k - pentagonal_numbers_list[i - 1] > D:
            break
        for j in range(i - 1, 0, -1):
            P_j = pentagonal_numbers_list[j]
            if P_k - P_j >= D:
                break
            while P_k + P_j > max_in_set:
                new_number = formula(len(pentagonal_numbers_list))
                pentagonal_numbers_list.append(new_number)
                pentagonal_numbers_set.add(new_number)
                max_in_set = new_number
            if P_k + P_j in pentagonal_numbers_set and P_k - P_j in pentagonal_numbers_set:
                D = P_k - P_j
    return D

print(f"{solution():,}")