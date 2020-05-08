N, K = map(int, input().split())
A = [-1] * N
for i in range(K):
    a, b = map(int, input().split())
    A[a-1] = b-1

dp = [[[0] * 3 for _ in range(3)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    for j in range(3):
        for k in range(3):
            source = [0, 1, 2]
            if A[i] >= 0:
                source = [A[i]]
            for v in source:
                if i >= 2 and v == j and j == k:
                    continue
                dp[i+1][k][v] += dp[i][j][k]

ans = 0
for d in dp[-1]:
    ans += sum(d)

print(ans%10000)
