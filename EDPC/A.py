N = int(input())
h = list(map(int, input().split()))

dp = [float("inf")] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])
for i in range(2, N):
    step1 = abs(h[i] - h[i-1])
    step2 = abs(h[i] - h[i-2])
    dp[i] = min(dp[i-1]+step1, dp[i-2]+step2)

print(dp[N-1])
