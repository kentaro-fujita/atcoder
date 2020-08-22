n = int(input())
a = list(map(int, input().split()))

res = 0
dp = [0] * n
for i in range(n):
    for j in range(i):
        dp[i] = max(dp[i], dp[j] + 1)
    res = max(res, dp[i])

print(res)
