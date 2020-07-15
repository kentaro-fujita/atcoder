N = int(input())

dp = [[0] * 3 for _ in range(N)]

for i in range(N):
    abc = list(map(int, input().split()))
    if i == 0:
        dp[i] = abc
    else:
        for j in range(3):
            dp[i][j] = max([dp[i-1][k] for k in range(3) if k != j]) + abc[j]

print(max(dp[N-1]))
