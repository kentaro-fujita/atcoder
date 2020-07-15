n, m = map(int, input().split())

dis = [[(float("inf"), 0)] * n for _ in range(n)]
for i in range(m):
    s, t, d, time = map(int, input().split())

    dis[s-1][t-1] = (d, time)
    dis[t-1][s-1] = (d, time)

dp = [[-1] * n for _ in range(1 << n)]
cnt = [[0] * n for _ in range(1 << n)]


def rec(s, v):
    if dp[s][v] > 0:
        return dp[s][v]

    if s == (1 << n) - 1 and v == 0:
        dp[s][v] = 0
        cnt[s][v] = 1
        return 0

    res = float("inf")
    for u in range(n):
        if not s >> u & 1:
            d, time = dis[v][u]
            ret = rec(s | (1 << u), u)
            if ret + d <= time:
                if ret + d < res:
                    res = ret + d
                    cnt[s][v] = cnt[s | (1 << u)][u]
                elif ret + d == res:
                    cnt[s][v] += cnt[s | (1 << u)][u]

    dp[s][v] = res
    return dp[s][v]


res = rec(0, 0)
if res == float("inf"):
    print("IMPOSSIBLE")
else:
    print(res, cnt[0][0])
print(dp)
print(cnt)
