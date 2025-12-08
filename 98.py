from collections import defaultdict
import itertools
import euler

def substitute(letters, permutation, word1, word2):
    substitution = {letter: num for letter, num in zip(letters, permutation)}

    # Replace each letter with a digit
    num1 = "".join(substitution[letter] for letter in word1)
    num2 = "".join(substitution[letter] for letter in word2)

    # Check for leading zeroes
    if num1[0] != "0" and num2[0] != "0":
        num1 = int(num1)
        num2 = int(num2)

        if euler.is_square(num1) and euler.is_square(num2):
            return max(num1, num2)

    return -1

# Return the largest square number that can be formed
# from word1 and word2 or -1 if not possible
def square_anagram(word1, word2):
    letters = list(set(word1))
    digits = "0123456789"

    return max(
        substitute(letters, permutation, word1, word2)
        for permutation in itertools.permutations(digits, len(letters))
    )

def load_words():
    with open("0098_words.txt") as f:
        return f.readline().replace('"', '').split(",")

def find_word_pairs(words):
    anagrams = defaultdict(set)

    for word in words:
        anagrams["".join(sorted(word))].add(word)

    return (
        pair
        for word_set in anagrams.values()
        for pair in itertools.combinations(word_set, 2)
    )

def solution():
    words = load_words()
    word_pairs = find_word_pairs(words)

    return max(
        square_anagram(word1, word2)
        for word1, word2 in word_pairs
    )

print(solution())