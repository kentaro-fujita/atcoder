n, k = map(int, input().split())
r = list(map(int, input().split()))
r.sort()

ans = 0
ll = r[-k:]
m = len(ll)
for i in range(m):
    ans = (ans + ll[i]) / 2

print(ans)
