import heapq

n = int(input())

g = [[] for _ in range(n)]
for i in range(n-1):
    a, b, c = map(int, input().split())

    g[a-1].append((b-1, c))
    g[b-1].append((a-1, c))

q, k = map(int, input().split())

dis = [float("inf")] * n
dis[k-1] = 0
pq = [(0, k-1)]
while pq:
    d, node = heapq.heappop(pq)
    if d > dis[node]: continue

    for nxt, cost in g[node]:
        if d + cost < dis[nxt]:
            dis[nxt] = d + cost
            heapq.heappush(pq, (dis[nxt], nxt))

ans = []
for i in range(q):
    x, y = map(int, input().split())

    ans.append(dis[x-1]+dis[y-1])

print("\n".join(map(str, ans)))
