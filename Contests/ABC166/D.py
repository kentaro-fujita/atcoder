import numpy as np


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


X = int(input())
divisors = make_divisors(X)
for d in divisors:
    d1 = d
    d2 = X/d
    solves = np.roots([5, 10*d1, 10*d1**2, 5*d1**3, d1**4-d2])

    for s in solves:
        if s == s.conjugate():
            if s.real.is_integer():
                print(int(d1+s.real), int(s.real))
                # exit()
