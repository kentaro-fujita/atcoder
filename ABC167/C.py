N, M, X = map(int, input().split())

C = [0] * N
A = [[] for _ in range(N)]

for i in range(N):
    C[i], *A[i] = list(map(int, input().split()))

ans = float("inf")
for i in range(1<<N):
    S = []
    for j in range(N):
        if i & (1<<j):
            S.append(j)
    
    W = [0] * M
    for s in S:
        for j in range(M):
            W[j] += A[s][j]
    
    flag = True
    for j in range(M):
        if W[j] < X:
            flag = False
            break

    if flag:
        res = 0
        for s in S:
            res += C[s]
        ans = min(ans, res)

if ans == float("inf"):
    print(-1)
else:
    print(ans)
