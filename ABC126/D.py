import sys
sys.setrecursionlimit(500 * 500)

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N - 1)]

A = [[] for _ in range(N + 1)]

for edge in edges:
    A[edge[0]].append([edge[1], edge[2]])
    A[edge[1]].append([edge[0], edge[2]])

depth = [-1] * (N + 1)
depth[1] = 0


def dfs(A, s):
    for v in A[s]:
        if depth[v[0]] == -1:
            depth[v[0]] = depth[s] + v[1]
            dfs(A, v[0])


dfs(A, 1)
for d in depth[1:]:
    if d % 2 == 0:
        print(0)
    else:
        print(1)
