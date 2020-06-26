n = int(input())
s = list(input())

mod = 10**4 + 7
c = {"J": 1, "O": 2, "I": 4}

dp = [[0] * (1<<3) for _ in range(n)]

for i in range(1<<3):
    if i & 1 and i & c[s[0]]:
        dp[0][i] = 1

for i in range(n-1):
    for j in range(1<<3):
        if dp[i][j]:
            for k  in range(1<<3):
                if j & k and k & c[s[i+1]]:
                    dp[i+1][k] += dp[i][j]
                    dp[i+1][k] %= mod

print(sum(dp[-1]) % mod)
