n, k = map(int, input().split())
r = list(map(int, input().split()))
r.sort()

ans = 0
l = r[-k:]
m = len(l)
for i in range(m):
    ans = (ans + l[i]) / 2

print(ans)
