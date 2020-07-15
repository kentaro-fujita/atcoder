from collections import deque

n = int(input())

g = [[] for _ in range(n)]
for _ in range(n):
    u, k, *V = list(map(int, input().split()))
    V.sort()
    for v in V:
        g[u-1].append(v-1)
        # g[v-1].append(u-1)
d = [-1] * n
d[0] = 0

que = deque([])
que.append(0)
while que:
    v = que.popleft()
    for i in g[v]:
        if d[i] == -1:
            d[i] = d[v] + 1
            que.append(i)

for i in range(n):
    print(f'{i+1} {d[i]}')
