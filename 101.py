import numpy as np
import itertools

def solution():
    def get_FIT(degree):
        x.append(degree + 1)
        y.append(u(degree + 1))
        f = np.polynomial.Polynomial.fit(x, y, deg=degree).convert()
        f_rounded = np.polynomial.Polynomial(np.round(f.coef))
        for n in itertools.count(1):
            if f_rounded(n) != u(n):
                return f_rounded(n)

    u = np.polynomial.Polynomial([(-1)**i for i in range(11)])

    x = []
    y = []

    return sum(get_FIT(degree) for degree in range(u.degree()))

print(f"{solution():,.0f}")