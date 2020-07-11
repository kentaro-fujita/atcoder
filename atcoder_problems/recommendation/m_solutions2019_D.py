import heapq

n = int(input())

g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

c = list(map(lambda x: -int(x), input().split()))
heapq.heapify(c)
print(min(c) - sum(c))

ans = []
s = [-1] * n
leaf = -1
for i, a in enumerate(g):
    if len(a) == 1:
        leaf = i
        break

que = [leaf]
while que:
    t = que.pop()
    for e in g[t]:
        if s[e] == -1:
            s[e] = -heapq.heappop(c)
            que.append(e)

print(*s)
