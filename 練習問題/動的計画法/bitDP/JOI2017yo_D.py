from collections import Counter

n, m = map(int, input().split())

a = [0] * n
cs = [[0] * n for _ in range(m)]
for i in range(n):
    a[i] = int(input())
    cs[a[i]-1][i] = 1
cnt = Counter(a)

for i in range(m):
    for j in range(1, n):
        cs[i][j] += cs[i][j-1]

dp = [float("inf")] * (1 << m)
dp[0] = 0
for i in range(1 << m):
    d = 0
    for j in range(m):
        if i & (1 << j):
            d += cnt[j+1]

    for j in range(m):
        if not i & (1 << j):
            k = cs[j][d+cnt[j+1]-1]
            if 0 < d:
                k -= cs[j][d-1]
            dp[i + (1 << j)] = min(dp[i + (1 << j)], dp[i] + cnt[j+1] - k)
print(dp[(1 << m)-1])
