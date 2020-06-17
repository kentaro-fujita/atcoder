n, l = map(int, input().split())
x = list(map(int, input().split()))
t1, t2, t3 = map(int, input().split())

dp = [float("inf")] * (l+1)

dp[0] = 0
dp[1] = t1
h = 0
if x[h] == 1:
    dp[1] += t3
    h += 1

for i in range(2, l+1):
    dp[i] = min(dp[i-1]+t1, dp[i-2]+t1+t2)
    if i > 4:
        dp[i] = min(dp[i], dp[i-4]+t1+t2*3)
    
    if h < len(x) and i == x[h]:
        dp[i] = dp[i] + t3
        h += 1

print(min(dp[-1], dp[-2]+(t1+t2)//2, dp[-3]+(t1+t2*3)//2, dp[-4]+(t1+t2*5)//2))
