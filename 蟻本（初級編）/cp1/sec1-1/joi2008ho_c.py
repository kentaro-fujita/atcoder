from bisect import bisect_right

n, m = map(int, input().split())
p = [0] + [int(input()) for _ in range(n)]
p.sort()

l = [p[i]+p[j] for i in range(n+1) for j in range(i, n+1) if p[i]+p[j] <= m]
l.sort()

ans = 0
for x in l:
    y = l[bisect_right(l, m - x) - 1]
    ans = max(ans, x + y)

print(ans)
