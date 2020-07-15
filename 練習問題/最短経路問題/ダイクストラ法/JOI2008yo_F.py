import heapq

n, k = map(int, input().split())

ans = []
g = [[] for _ in range(n)]
for i in range(k):
    query = list(input().split())
    if query[0] == '0':
        _, a, b = map(int, query)
        dis = [float("inf") for _ in range(n)]
        dis[a-1] = 0

        pq = [(0, a-1)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dis[node]:
                continue

            for nxt, cost in g[node]:
                if d + cost < dis[nxt]:
                    dis[nxt] = d + cost
                    heapq.heappush(pq, (dis[nxt], nxt))

        res = dis[b-1]
        if res == float("inf"):
            ans.append(-1)
        else:
            ans.append(res)
    if query[0] == '1':
        _, c, d, e = map(int, query)
        g[c-1].append((d-1, e))
        g[d-1].append((c-1, e))

print(*ans, sep='\n')
