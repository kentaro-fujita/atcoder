n, m, q = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

c = list(map(int, input().split()))

ans = []
for i in range(q):
    query = input().split()
    if query[0] == '1':
        x = int(query[1])
        ans.append(c[x-1])
        for e in g[x-1]:
            c[e] = c[x-1]
    if query[0] == '2':
        x, y = map(int, query[1:])
        ans.append(c[x-1])
        c[x-1] = y

print('\n'.join(map(str, ans)))
