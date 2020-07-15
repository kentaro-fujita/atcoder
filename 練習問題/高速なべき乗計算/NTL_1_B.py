mod = 10**9 + 7


def pow(x, y):
    ret = 1
    while y:
        if y & 1:
            ret = ret * x % mod
        x = x * x % mod
        y >>= 1

    return ret


m, n = map(int, input().split())
print(pow(m, n))
