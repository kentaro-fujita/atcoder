n = int(input())
a = [int(input()) for _ in range(n)]

dp = [0] * n
for i in range(1, n):
    dp[i] = max(a[i-1]//2, min(a[i-1], a[i]))

print(dp)
