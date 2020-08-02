w = int(input())
n, k = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

dp = [[[float("inf")] * (w+1) for _ in range(k+1)] for _ in range(n+1)]
dp[0][0][0] = 0

for x in range(n):
    for y in range(k+1):
        for z in range(w+1):
            dp[x+1][y][z] = min(dp[x+1][y][z], dp[x][y][z])
            if y + 1 <= k and z + b[x] <= w:
                dp[x+1][y+1][z+b[x]] = min(dp[x+1]
                                           [y+1][z+b[x]], dp[x][y][z] + a[x])

ans = 0
for i in range(k+1):
    for j in range(w+1):
        ans = max(ans, dp[n][i][j])

print(ans)
