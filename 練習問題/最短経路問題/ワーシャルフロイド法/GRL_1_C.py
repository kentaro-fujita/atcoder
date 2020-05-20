V, E = map(int, input().split())

dp = [[float("inf")] * V for _ in range(V)]

for i in range(V):
    dp[i][i] = 0

for _ in range(E):
    s, t, d = map(int, input().split())
    dp[s][t] = d

for k in range(V):
    for i in range(V):
        for j in range(V):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            if i == j and dp[i][i] < 0:
                print("NEGATIVE CYCLE")
                exit()

for i in range(V):
    ans = []
    for j in range(V):
        if dp[i][j] == float("inf"):
            ans.append("INF")
        else:
            ans.append(dp[i][j])
    print(*ans)
