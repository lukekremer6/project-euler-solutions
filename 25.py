import itertools

def fibonacci():
    a = 1
    b = 1
    for i in itertools.count(1):
        if len(str(a)) == 1000:
            return i
        a, b = b, a + b

print(fibonacci())