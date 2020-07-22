from collections import deque

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
white_count = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            white_count += 1

d = [[float("inf")] * w for _ in range(h)]

que = deque()
que.append((0, 0))
d[0][0] = 1
while que:
    x, y = que.popleft()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < w and 0 <= ny < h and s[ny][nx] == '.' and d[ny][nx] == float("inf"):
            que.append((nx, ny))
            d[ny][nx] = d[y][x] + 1

res = d[h-1][w-1]
if res == float("inf"):
    print(-1)
else:
    print(white_count - res)
