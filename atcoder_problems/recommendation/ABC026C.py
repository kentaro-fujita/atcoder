import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())

g = [[] for _ in range(n)]
for i in range(n-1):
    b = int(input())
    g[b-1].append(i+1)

s = [0] * n


def dfs(g, v):
    s[v] = 1
    if not g[v]:
        return 1
    res = []
    for e in g[v]:
        if s[e] == 0:
            res.append(dfs(g, e))
    return max(res) + min(res) + 1


print(dfs(g, 0))
