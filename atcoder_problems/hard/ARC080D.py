h, w = map(int, input().split())
n = int(input())
a = [0] + list(map(int, input().split()))

ans = [[] for _ in range(h)]
k = 1
for i in range(h):
    row = []
    for j in range(w):
        if not a[k]: k += 1
        row.append(k)
        a[k] -= 1
    if i % 2 == 1:
        ans[i] = list(reversed(row))
    else:
        ans[i] = row

for i in range(h):
    print(*ans[i])
