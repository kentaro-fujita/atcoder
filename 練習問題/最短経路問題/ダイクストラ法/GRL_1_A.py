import heapq

V, E, r = map(int, input().split())

g = [[] for _ in range(V)]
for i in range(E):
    s, t, d = map(int, input().split())
    g[s].append((t, d))

dis = [float("inf") for _ in range(V)]
dis[r] = 0

pq = [(0, r)]
while pq:
    d, node = heapq.heappop(pq)
    if d > dis[node]:
        continue

    for nxt, cost in g[node]:
        if d + cost < dis[nxt]:
            dis[nxt] = d + cost
            heapq.heappush(pq, (dis[nxt], nxt))

for d in dis:
    if d == float("inf"):
        print("INF")
    else:
        print(d)
