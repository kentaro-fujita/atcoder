def power(a, n):
    x = 1
    while n:
        if n & 1:
            x *= a
        if x > 10**9:
            return 10**9+1
        n >>= 1
        a *= a
    return x


a, r, n = map(int, input().split())

ans = a * power(r, n-1)
if ans > 10**9:
    print('large')
else:
    print(ans)
