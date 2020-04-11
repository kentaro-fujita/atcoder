N = int(input())
p = list(map(int, input().split()))

_sum = sum(p)
dp = [[False]*(_sum+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(_sum+1):
        if p[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-p[i-1]]

print(sum(dp[N]))