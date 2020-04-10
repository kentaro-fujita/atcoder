from bisect import bisect_left

n = int(input())
wh = [list(map(int, input().split())) for _ in range(n)]
wh.sort(key = lambda x : (x[0], -x[1]))

INF = 10**9
dp = [INF for _ in range(n+1)]
for i in range(n):
    dp[bisect_left(dp, wh[i][1])] = wh[i][1]

print(bisect_left(dp, INF))