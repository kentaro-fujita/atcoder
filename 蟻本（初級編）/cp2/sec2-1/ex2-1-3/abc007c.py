from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

que = deque()
d = [[float("inf")] * C for _ in range(R)]
que.append([sx-1, sy-1])
d[sy-1][sx-1] = 0

while que:
    px, py = que.popleft()
    if px == gx-1 and py == gy-1:
        break
    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i]
        if 0 <= nx < C and 0 <= ny < R and c[ny][nx] != '#' and d[ny][nx] == float("inf"):
            que.append((nx, ny))
            d[ny][nx] = d[py][px] + 1
print(d[gy-1][gx-1])
