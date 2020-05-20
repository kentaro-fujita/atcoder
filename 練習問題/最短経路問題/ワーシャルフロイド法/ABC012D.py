n, m = map(int, input().split())

dp = [[float("inf")] * n for _ in range(n)]
for i in range(m):
    a, b, t = map(int, input().split())
    
    dp[a-1][b-1] = t
    dp[b-1][a-1] = t

for i in range(n):
    dp[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = float("inf")
for i in range(n):
    ans = min(ans, max(dp[i]))

print(ans)
