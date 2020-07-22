n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [float("inf")] * (n+1)
dp[0] = 0
for i in range(1, n + 1):
    for j in range(m):
        if i >= c[j]:
            dp[i] = min(dp[i], dp[i-c[j]]+1)

print(dp[n])
