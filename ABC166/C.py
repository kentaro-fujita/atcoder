n, m = map(int, input().split())
H = list(map(int, input().split()))

g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

ans = 0
for i in range(n):
    flag = True
    if len(g[i]) == 0:
        ans += 1
    else:
        for v in g[i]:
            if H[v] >= H[i]:
                flag = False
                break
        if flag:
            ans += 1

print(ans)