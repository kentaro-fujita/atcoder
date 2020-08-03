N, M, K = map(int, input().split())
F = [[] for _ in range(N)]
B = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    F[a-1].append(b-1)
    F[b-1].append(a-1)

for i in range(K):
    c, d = map(int, input().split())
    B[c-1].append(d-1)
    B[d-1].append(c-1)

D = {}
parent = [-1] * N
visited = [False] * N
for root in range(N):
    if visited[root]:
        continue

    D[root] = set([root])
    stack = [root]
    while stack:
        n = stack.pop()
        visited[n] = True
        parent[n] = root

        for to in F[n]:
            if visited[to]:
                continue
            D[root].add(to)
            stack.append(to)

ans = [0] * N
for iam in range(N):
    group = D[parent[iam]]
    tmp_ans = len(group) - len(F[iam]) - 1
    for block in B[iam]:
        if block in group:
            tmp_ans -= 1
    ans[iam] = tmp_ans

print(*ans, sep=' ')
