from collections import deque

H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

block_count = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            block_count += 1

d = [[0] * W for _ in range(H)]

dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

que = deque([])
que.append((0, 0))
d[0][0] = 1
while que:
    x, y = que.popleft()

    for dx, dy in dxdy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < W and 0 <= ny < H and d[ny][nx] == 0 and s[ny][nx] == '.':
            que.append((nx, ny))
            d[ny][nx] = d[y][x] + 1

if d[H-1][W-1]:
    print(H * W - d[H-1][W-1] - block_count)
else:
    print(-1)
