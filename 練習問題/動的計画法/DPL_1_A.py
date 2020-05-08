n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [[float("inf")] * (n+1) for _ in range(m)]

for i in range(m):
    dp[i][0] = 0
for j in range(n+1):
    dp[0][j] = j

for i in range(1, m):
    for j in range(1, n+1):
        if c[i] > j:
            dp[i][j] = min(dp[i][j], dp[i-1][j])
        else:
            dp[i][j] = min(dp[i][j], dp[i][j-c[i]]+1)

print(dp)
print(dp[m-1][n])
