N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

dp = [[float("inf")] * (N+1) for _ in range(M+1)]
dp[0][0] = 0

for i in range(M):
    for j in range(N):
        dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + C[i] * D[j])
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

ans = float("inf")
for i in range(M+1):
    ans = min(ans, dp[i][N])

print(ans)
