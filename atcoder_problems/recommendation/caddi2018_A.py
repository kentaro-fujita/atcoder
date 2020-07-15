def prime_factorize(n):
    res = []
    for i in range(2, int(n**(1/2))+1):
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


n, p = map(int, input().split())

prime = prime_factorize(p)

ans = 1
for k, v in prime:
    ans *= k ** (v // n)

print(int(ans))
