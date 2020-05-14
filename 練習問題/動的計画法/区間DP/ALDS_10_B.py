n = int(input())

M = []
for i in range(n):
    r, c = map(int, input().split())
    if i == 0: M.append(r)
    M.append(c)

dp = [[float("inf")] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][i] = 0

for l in range(2, n+1):
    for i in range(1,n-l+2):
        j = i + l -1
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + M[i-1]*M[k]*M[j])

print(dp[1][n])
