MAX_N = 44
dp = [None] * (MAX_N + 1)
dp[0] = 1
dp[1] = 1

def fib(n):
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

n = int(input())
print(fib(n))