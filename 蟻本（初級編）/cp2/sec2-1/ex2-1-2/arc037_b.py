n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

s = [0] * n


def dfs(now, prev):
    global flag
    s[now] = 1
    for nxt in g[now]:
        if nxt != prev:
            if s[nxt] == 1:
                flag = False
            else:
                dfs(nxt, now)


ans = 0
for i in range(n):
    if s[i] == 0:
        flag = True
        dfs(i, -1)
        if flag:
            ans += 1

print(ans)
