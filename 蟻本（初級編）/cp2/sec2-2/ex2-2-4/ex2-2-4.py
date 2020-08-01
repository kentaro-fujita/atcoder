while True:
    r, n = map(int, input().split())
    if n == -1 and r == -1:
        break
    x = list(map(int, input().split()))
    x.sort()

    i = 0
    ans = 0
    while i < n:
        s = x[i]
        while i < n and x[i] <= s + r:
            i += 1
        p = x[i - 1]
        while i < n and x[i] <= p + r:
            i += 1
        ans += 1

    print(ans)
