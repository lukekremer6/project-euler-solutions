import itertools

def decrypt(ciphertext, key):
    decrypted_data = [byte ^ key[i % len(key)] for i, byte in enumerate(ciphertext)]
    return "".join(chr(byte) for byte in decrypted_data)

def count_common_words(plaintext):
    common_words = (
        "the", "be", "to", "of", "and",
        "in", "that", "have", "it", "for"
    )
    return sum(plaintext.count(word) for word in common_words)

def solution():
    with open("0059_cipher.txt") as f:
        ciphertext = [int(num) for num in f.readline().split(",")]
        alphabet = list(range(ord("a"), ord("a") + 26))
        best_key = max(
            [k for k in itertools.product(alphabet, repeat=3)],
            key=lambda k: count_common_words(decrypt(ciphertext, k))
        )
        plaintext = decrypt(ciphertext, best_key)
        return sum(ord(char) for char in plaintext)

print(f"{solution():,}")