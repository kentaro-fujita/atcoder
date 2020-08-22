s = list(input())
n = len(s)
t = list(input())
m = len(t)
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = i

for j in range(m+1):
    dp[0][j] = j

for i in range(n):
    for j in range(m):
        cost = 0 if s[i] == t[j] else 1
        dp[i+1][j+1] = min(dp[i][j+1] + 1, dp[i+1][j] + 1, dp[i][j] + cost)

print(dp[n][m])
