from collections import deque

ans = []
while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    col = []
    row = []
    for i in range(2*h-1):
        if i % 2 == 0:
            col.append(list(map(int, input().split())))
        else:
            row.append(list(map(int, input().split())))

    dwdh = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    d = [[0] * w for _ in range(h)]

    que = deque([(0, 0)])
    d[0][0] = 1
    while que:
        qw, qh = que.popleft()

        for dw, dh in dwdh:
            nw = qw + dw
            nh = qh + dh
            if not(0 <= nh < h) or not(0 <= nw < w) or d[nh][nw]:
                continue
            if (dh == -1 and row[nh][nw] == 1) or (dh == 1 and row[nh-1][nw] == 1):
                continue
            if (dw == -1 and col[nh][nw] == 1) or (dw == 1 and col[nh][nw-1] == 1):
                continue

            que.append((nw, nh))
            d[nh][nw] = d[qh][qw] + 1

    ans.append(d[h-1][w-1])

for a in ans:
    print(a)
