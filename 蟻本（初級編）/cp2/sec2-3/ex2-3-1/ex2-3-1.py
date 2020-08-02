N, W = map(int, input().split())
v = [0] * N
w = [0] * N
for i in range(N):
    v[i], w[i] = map(int, input().split())

dp = [[0] * (W+1) for _ in range(N)]

for i in range(N):
    for j in range(1, W+1):
        if w[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v[i]+dp[i-1][j-w[i]])

print(max(dp[N-1]))
