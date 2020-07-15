n = int(input())
xy = set([tuple(map(int, input().split())) for _ in range(n)])

res = 0

for x1, y1 in xy:
    for x2, y2 in xy:
        dx = x2 - x1
        dy = y2 - y1

        if (x1 + dy, y1 - dx) in xy and (x2 + dy, y2 - dx) in xy:
            res = max(res, dx ** 2 + dy ** 2)

print(res)
