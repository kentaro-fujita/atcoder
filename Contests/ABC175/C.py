x, k, d = map(int, input().split())
x = abs(x)

m = x // d
if k <= m:
    print(x - k * d)
else:
    n = (k - m) % 2
    print(abs(x - d * m - d * n))
