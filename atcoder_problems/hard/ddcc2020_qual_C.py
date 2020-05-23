h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]

a = [[0] * w for _ in range(h)]
cnt = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            cnt += 1 
            a[i][j] = cnt
        elif j >= 1 and a[i][j-1] > 0:
            a[i][j] = a[i][j-1]
    if a[i][0] == 0:
        for j in range(w-2, -1, -1):
            if a[i][j] == 0:
                a[i][j] = a[i][j+1]

for i in range(h-2, -1, -1):
    if a[i][0] == 0:
        for j, v in enumerate(a[i+1]):
            a[i][j] = v
for i in range(h):
    if a[i][j] == 0:
        for j, v in enumerate(a[i-1]):
            a[i][j] = v

for i in range(h):
    print(*a[i])
