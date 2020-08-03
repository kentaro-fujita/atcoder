from collections import deque

N, Q = map(int, input().split())

g = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

cnt = [0] * N
for i in range(Q):
    p, x = map(int, input().split())
    cnt[p - 1] += x

que = deque([])
que.append(0)
s = [0] * N
while que:
    t = que.popleft()
    s[t] = 1
    for e in g[t]:
        if s[e] == 1:
            continue
        cnt[e] += cnt[t]
        que.append(e)

print(*cnt)
