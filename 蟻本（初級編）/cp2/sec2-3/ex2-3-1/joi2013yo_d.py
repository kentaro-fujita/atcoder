d, n = map(int, input().split())
t = [int(input()) for _ in range(d)]

a = [0] * n
b = [0] * n
c = [0] * n
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())

dp = [[-float("inf")] * n for _ in range(d)]
for i in range(d):
    for j in range(n):
        if a[j] <= t[i] <= b[j]:
            if i == 0:
                dp[i][j] = 0
            else:
                for k in range(n):
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(c[k] - c[j]))

print(max(dp[-1]))
