from bisect import bisect_right

n = int(input())

six = [0] + [6**i for i in range(1,8)]
nine = [0] + [9**i for i in range(1,7)]

dp = [float("inf")] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    dp[i] = dp[i-1] + 1
    j = bisect_right(six, i) - 1
    if j: dp[i] = min(dp[i], dp[i-six[j]] + 1)
    k = bisect_right(nine, i) - 1
    if k: dp[i] = min(dp[i], dp[i-nine[k]] + 1)

print(dp[-1])
