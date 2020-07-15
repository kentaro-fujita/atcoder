N, W = map(int, input().split())
w = [0] * N
v = [0] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())

dp = [0] + [float("inf")] * 10**5

for i in range(N):
    for j in range(10**5, v[i]-1, -1):
        dp[j] = min(dp[j], dp[j-v[i]] + w[i])

res = 0
for v, e in enumerate(dp):
    if e <= W:
        res = v

print(res)
