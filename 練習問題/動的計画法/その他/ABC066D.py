from bisect import bisect_left

n = int(input())
c = [int(input()) for _ in range(n)]

dp = [c[0]]
for i in range(n):
    if dp[-1] < c[i]:
        dp.append(c[i])
    else:
        dp[bisect_left(dp, c[i])] = c[i]

print(n - len(dp))
