N, M, Q = map(int, input().split())

prob = [0] * M
is_solve = [[0] * M for _ in range(N)]
ans = []
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        n = int(query[1])
        ans.append(sum([N - prob[j] for j in range(M) if is_solve[n-1][j]]))
    elif query[0] == '2':
        n, m = map(int, query[1:])
        prob[m-1] += 1
        is_solve[n-1][m-1] = 1

print("\n".join(map(str, ans)))
