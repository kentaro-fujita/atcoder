N, M = map(int, input().split())

isSafe = [True] * (N + 1)
for _ in range(M):
    a = int(input())
    isSafe[a] = False

dp = [0] * (N + 1)

dp[0] = 1
dp[1] = 1
for i in range(2, N + 1):
    if isSafe[i - 1]:
        dp[i] += dp[i - 1]
    if isSafe[i - 2]:
        dp[i] += dp[i - 2]

print(dp[N] % (10**9 + 7))
