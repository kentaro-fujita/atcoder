D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
X = [list(map(int, input().split())) for _ in range(N)]
A, B, C = map(list, zip(*X))

dp = [[-float("inf")] * N for _ in range(D)]

for i in range(D):
    for j in range(N):
        if A[j] <= T[i] <= B[j]:
            if i == 0:
                dp[i][j] = 0
            else:
                for k in range(N):
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(C[k] - C[j]))

print(max(dp[D-1]))
