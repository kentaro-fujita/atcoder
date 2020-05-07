from collections import deque

N = int(input())

g = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    g[a-1].append((b-1, i))
    g[b-1].append((a-1, i))

max_color = 0
for i in range(N):
    max_color = max(max_color, len(g[i]))

res = [-1] * (N-1)
d = [-1] * N
que = deque([])
que.append((0, -1))
d[0] = 0
while que:
    v, c = que.popleft()
    color = 1
    if color == c:
        color += 1
    for f, s in g[v]:
        if d[f] == -1:
            d[f] = d[v] + 1
            que.append((f, color))
            res[s] = color
            color += 1
            if color == c:
                color += 1

print(max_color)
for v in res:
    print(v)
