from collections import deque

n, q = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

c = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    c[p-1] += x

q = deque([0])
flag = [False] * n
while q:
    v = q.pop()
    flag[v] = True
    for e in g[v]:
        if flag[e]:
            continue
        c[e] += c[v]
        q.append(e)

print(*c)
