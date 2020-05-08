import numpy as np

N = int(input())
S = [list(input()) for _ in range(5)]
s = (np.array(S).T).tolist()
color = {'R': 0, 'B': 1, 'W':2, '#': 3}

dp = [[float("inf")] * 3 for _ in range(N)]

lst = [s[0].count("R"), s[0].count("B"), s[0].count("W")]
for i in range(3):
    dp[0][i] = 5 - lst[i]

for i in range(N-1):
    lst = [s[i+1].count("R"), s[i+1].count("B"), s[i+1].count("W")]
    for j in range(3):
        for k in range(3):
            if j == k: continue
            dp[i+1][k] = min(dp[i+1][k], dp[i][j] + (5 - lst[k]))

print(min(dp[N-1]))
