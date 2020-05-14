N = int(input())
A = [int(input()) for _ in range(N)]
A = A * 2

dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if j == N-1:
            j = -1
        k = j + i
        if i % 2 == 1:
            if A[j] >= A[k+1]:
                dp[i][j] = max(dp[i-1][j+1], dp[i][j])
            if A[k] >= A[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j])
        else:
            dp[i][j] = max(dp[i-1][j+1]+A[j], dp[i-1][j]+A[k])

print(max(dp[-1]))
