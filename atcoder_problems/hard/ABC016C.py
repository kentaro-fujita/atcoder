n, m = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

for i in range(n):
    ans = []
    for x in g[i]:
        for y in g[x]:
            if y != i and y not in g[i]:
                ans.append(y)

    print(len(set(ans)))
