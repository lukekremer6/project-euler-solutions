def word_value(s):
    return sum(ord(char) - ord("A") + 1 for char in s)

def get_triangle_numbers(n):
    result = set()
    i = 1
    current = 1
    while current < n:
        current = i * (i + 1) // 2
        result.add(current)
        i += 1
    return result

def solution():
    with open("0042_words.txt") as f:
        words = [word[1:-1] for word in f.readline().split(",")]
        max_word = max(words, key=word_value)
        triangle_numbers = get_triangle_numbers(word_value(max_word))
        return sum(1 for word in words if word_value(word) in triangle_numbers)

print(f"{solution():,}")