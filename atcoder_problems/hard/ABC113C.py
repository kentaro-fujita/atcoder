n, m = map(int, input().split())

pre = [[] for _ in range(n)]
for i in range(m):
    p, y = map(int, input().split())
    pre[p-1].append((i, y))

c = []
for x, p in enumerate(pre):
    p.sort(key=lambda x: x[1])

    for j, (i, y) in enumerate(p):
        c.append((i, x+1, j+1))

c.sort(key=lambda x: x[0])
for _, x, y in c:
    print(str(x).zfill(6)+str(y).zfill(6))
