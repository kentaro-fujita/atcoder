from itertools import combinations

n, m = map(int, input().split())

g = [[0] * n for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    g[x-1][y-1] = 1
    g[y-1][x-1] = 1

ans = 0
for i in range(1 << n):
    group = []
    for j in range(n):
        if i & 1 << j:
            group.append(j)
    flag = True
    for comb in combinations(group, 2):
        x, y = comb
        if g[x][y] == 0:
            flag = False
            break
    if flag:
        ans = max(ans, len(group))
print(ans)
