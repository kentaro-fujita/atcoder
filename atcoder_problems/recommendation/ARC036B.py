from collections import defaultdict

n = int(input())
h = [int(input()) for _ in range(n)]

u = defaultdict(int)
d = defaultdict(int)
l = 0
r = 0
i = 0
for i in range(1, n):
    if h[i-1] < h[i]:
        d[r] = i - r
        r = i
    else:
        u[i-1] = i - l
        l = i
d[r] = i + 1 - r
u[i] = i + 1 - l

ans = 0
for k, v in u.items():
    ans = max(ans, v + d[k] - 1)

print(ans)
