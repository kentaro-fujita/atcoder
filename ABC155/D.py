n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

INF = 1 << 61
left = -INF
right = INF
while right - left > 1:
    x = (left + right) // 2
    s = 0
    t = 0
    for i in range(n):
        if a[i] > 0:
            l2 = -1
            r2 = n
            while r2 - l2 > 1:
                m = (l2 + r2) // 2
                if a[i] * a[m] <= x:
                    l2 = m
                else:
                    r2 = m
            s += r2
        elif a[i] < 0:
            l2 = -1
            r2 = n
            while r2 - l2 > 1:
                m = (l2 + r2) // 2
                if a[i] * a[m] <= x:
                    r2 = m
                else:
                    l2 = m
            s += n - r2
        elif x >= 0:
            s += n
        if a[i] * a[i] <= x:
            t += 1
    num = (s - t) // 2
    if num >= k:
        right = x
    else:
        left = x
print(right)
