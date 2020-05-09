N = int(input())
*num, ans = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N-1)]
dp[0][num[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if j + num[i] < 21:
            dp[i][j+num[i]] += dp[i-1][j]
        if j - num[i] >= 0:
            dp[i][j-num[i]] += dp[i-1][j]

print(dp[N-2][ans])
