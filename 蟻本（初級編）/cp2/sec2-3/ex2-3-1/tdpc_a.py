n = int(input())
p = list(map(int, input().split()))
m = sum(p)

dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if p[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-p[i-1]]

print(sum(dp[n]))
