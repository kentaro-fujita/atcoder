def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def prime_factorize(n):
    res = []
    for i in range(2, int(n**(1 / 2)) + 1):
        if n % i != 0:
            continue
        num = 0
        while n % i == 0:
            num += 1
            n /= i
        res.append((i, num))
    if n != 1:
        res.append((n, 1))

    return res


A, B = map(int, input().split())

gcdAB = gcd(A, B)
pf = prime_factorize(gcdAB)

print(len(pf) + 1)
