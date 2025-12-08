from collections import Counter
import math

pan_digital = Counter("123456789")

def is_pan_digital(a, b, c):
    s = str(a) + str(b) + str(c)
    return Counter(s) == pan_digital

def solution():
	result = 0
	for c in range(1, 10_000):
		for a in range(2, math.isqrt(c)):
			if c % a == 0 and is_pan_digital(a, c // a, c):
				result += c
				break
	return result

print(f"{solution():,}")