from collections import deque

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())

    g[a-1].append(b-1)
    g[b-1].append(a-1)

d = [-1] * n
d[0] = 0
b = [[] for _ in range(n)]
q = deque([0])
while q:
    v = q.popleft()
    for e in g[v]:
        if d[e] == -1:
            d[e] = d[v] + 1
            b[e].append(v)
            q.append(e)

if -1 in d:
    print("No")
else:
    print("Yes")
    for i in range(1, n):
        print(b[i][0]+1)
