n, m, x = map(int, input().split())
c = [0] * n
a = [[0] * m for _ in range(n)]
for i in range(n):
    c[i], *a[i] = map(int, input().split())

ans = float("inf")
for i in range(1<<n):
    t = [0] * m
    cost = 0
    for j in range(n):
        if i & (1<<j):
            cost += c[j]
            for k in range(m):
                t[k] += a[j][k]
    if min(t) >= x:
        ans = min(ans, cost)

if ans == float("inf"):
    print(-1)
else:
    print(ans)
