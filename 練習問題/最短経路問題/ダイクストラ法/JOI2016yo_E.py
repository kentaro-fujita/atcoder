import heapq
from collections import deque

n, m, k, s = map(int, input().split())
p, q = map(int, input().split())

c = [int(input()) - 1 for _ in range(k)]

g = [[] for _ in range(n)]
ab = [list(map(int, input().split())) for _ in range(m)]
for a, b in ab:
    g[a-1].append(b-1)
    g[b-1].append(a-1)


d = [float("inf")] * n
que = deque(c)
for v in c:
    d[v] = 0
while que:
    t = que.popleft()
    for e in g[t]:
        if d[e] != float("inf"): continue
        d[e] = d[t] + 1
        que.append(e)

cost = [p] * n
for i in range(n):
    if d[i] <= s:
        cost[i] = q
    if i in c:
        cost[i] = float("inf")
    if n == 0 or i == n-1:
        cost[i] = 0

dis = [float("inf") for _ in range(n)]
dis[0] = 0

pq = [(0, 0)]
while pq:
    d, node = heapq.heappop(pq)
    if d > dis[node]: continue

    for nxt in g[node]:
        if d + cost[nxt] < dis[nxt]:
            dis[nxt] = d + cost[nxt]
            heapq.heappush(pq, (dis[nxt], nxt))

print(dis[-1])
