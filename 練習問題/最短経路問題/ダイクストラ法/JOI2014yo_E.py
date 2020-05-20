import heapq
from collections import deque

n, k = map(int, input().split())
cr = [list(map(int, input().split())) for _ in range(n)]

g = [[] for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

ng = [[] for _ in range(n)]
for i in range(n):
    d = [-1] * n
    d[i] = 0
    que = deque([i])
    while que:
        t = que.popleft()
        for e in g[t]:
            if d[e] != -1: continue
            d[e] = d[t] + 1
            que.append(e)

    ng[i] = [j for j in range(n) if 0 < d[j] <= cr[i][1]]

dis = [float("inf")] * n
dis[0] = 0
pq = [(0, 0)]
while pq:
    _, u = heapq.heappop(pq)
    for v in ng[u]:
        if dis[u] + cr[u][0] < dis[v]:
            dis[v] = dis[u] + cr[u][0]
            heapq.heappush(pq, (dis[v], v))

print(dis[-1])
