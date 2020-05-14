N, M, Q = map(int, input().split())

s = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    l, r = map(int, input().split())
    s[l][r] += 1

for i in range(1, N+1):
    for j in range(1, N+1):
        s[i][j] += s[i-1][j] + s[i][j-1] - s[i-1][j-1]

for _ in range(Q):
    p, q = map(int, input().split())

    print(s[q][q] - s[q][p-1] - s[p-1][q] + s[p-1][p-1])
