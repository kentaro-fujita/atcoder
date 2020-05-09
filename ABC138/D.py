from collections import deque

N, Q = map(int, input().split())

g = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    print(a,b)
    g[a-1].append(b-1)
    g[b-1].append(a-1)

c = [0] * N
for i in range(Q):
    p, x = map(int, input().split())

    que = deque([])
    que.append(p-1)
    while que:
        t = que.popleft()
        c[t] += x
        for e in g[t]:
            que.append(e)

for v in c:
    print(v)
