h, n = map(int, input().split())

A = [0] * n
B = [0] * n
for i in range(n):
    A[i], B[i] = map(int, input().split())

dp = [float("inf")] * (h+1)
dp[0] = 0

for i in range(h):
    for j in range(n):
        next_index = min(i + A[j], h)
        dp[next_index] = min(dp[next_index], dp[i] + B[j])

print(dp[-1])
