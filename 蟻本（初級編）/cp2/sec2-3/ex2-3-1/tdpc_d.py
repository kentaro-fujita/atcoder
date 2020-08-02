n, d = map(int, input().split())

cnt = []
for v in [2, 3, 5]:
    c = 0
    while d % v == 0:
        c += 1
        d //= v
    cnt.append(c)

if d != 1:
    print(0)
    exit()

p2, p3, p5 = cnt

dp = [[[[0] * (p5+1) for _ in range(p3+1)]
       for _ in range(p2+1)] for _ in range(n+1)]
dp[0][0][0][0] = 1
for i in range(n):
    for j in range(p2+1):
        for k in range(p3+1):
            for l in range(p5+1):
                dp[i+1][j][k][l] += dp[i][j][k][l] / 6
                dp[i+1][min(j+1, p2)][k][l] += dp[i][j][k][l] / 6
                dp[i+1][j][min(k+1, p3)][l] += dp[i][j][k][l] / 6
                dp[i+1][min(j+2, p2)][k][l] += dp[i][j][k][l] / 6
                dp[i+1][j][k][min(l+1, p5)] += dp[i][j][k][l] / 6
                dp[i+1][min(j+1, p2)][min(k+1, p3)][l] += dp[i][j][k][l] / 6

print(dp[n][p2][p3][p5])
