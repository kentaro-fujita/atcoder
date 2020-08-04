d = int(input())
n = list(input())
m = len(n)
mod = 10**9 + 7

dp = [[[0] * d for _ in range(2)] for _ in range(m + 1)]
dp[0][0][0] = 1

for i in range(m):
    num = int(n[i])
    for j in range(10):
        for k in range(d):
            dp[i + 1][1][(k + j) % d] = (dp[i + 1][1][(k + j) % d] + dp[i][1][k]) % mod
    for j in range(num):
        for k in range(d):
            dp[i + 1][1][(k + j) % d] = (dp[i + 1][1][(k + j) % d] + dp[i][0][k]) % mod
    for j in range(d):
        dp[i + 1][0][(j + num) % d] = (dp[i + 1][0][(j + num) % d] + dp[i][0][j]) % mod

print((dp[m][1][0] + dp[m][0][0] - 1) % mod)
