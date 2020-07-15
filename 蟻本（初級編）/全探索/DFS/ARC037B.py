def dfs(now, prev):
    global flag

    for next in g[now]:
        if next != prev:
            if memo[next]:
                flag = False
            else:
                memo[next] = True
                dfs(next, now)


N, M = map(int, input().split())

g = [[] * N for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

memo = [False for _ in range(N)]

ans = 0
for i in range(N):
    if not memo[i]:
        flag = True
        dfs(i, -1)
        if flag:
            ans += 1

print(ans)
