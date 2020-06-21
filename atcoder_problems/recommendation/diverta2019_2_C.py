n = int(input())
a = list(map(int, input().split()))
a.sort()

res = []
low, up = a[0], a[-1]
for i in range(1, n-1):
    if a[i] < 0:
        res.append([up, low])
        up = up - low
        low = a[i]
    else:
        res.append([low, up])
        low = low - up
        up = a[i]

print(up-low)
res.append([up, low])

for v in res:
    print(*v)
