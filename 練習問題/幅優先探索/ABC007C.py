from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = [[float("inf")] * C for _ in range(R)]

que = deque([])
que.append((sx-1, sy-1))
d[sy-1][sx-1] = 0
while que:
    x, y = que.popleft()

    if (x, y) == (gx-1, gy-1):
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < C and 0 <= ny < R and c[ny][nx] == "." and d[ny][nx] == float("inf"):
            que.append((nx, ny))
            d[ny][nx] = d[y][x] + 1

print(d[gy-1][gx-1])