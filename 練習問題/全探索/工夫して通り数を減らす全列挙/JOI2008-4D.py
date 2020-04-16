m = int(input())
txy = [tuple(map(int, input().split())) for _ in range(m)]
n = int(input())
pxy = [tuple(map(int, input().split())) for _ in range(n)]

bx, by = txy[0]

tvec = set()
for i in range(1, m):
    tx, ty = txy[i]
    tvec.add((tx - bx, ty - by))

for i in range(n):
    px, py = pxy[i]
    pvec = set()
    for j in range(n):
        if i != j:
            qx, qy = pxy[j]
            pvec.add((qx - px, qy - py))
    if pvec >= tvec:
        print(px - bx, py - by)
        exit()
