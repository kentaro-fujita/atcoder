from collections import deque

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
s = [[float("inf")] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            sx, sy = j, i
        if c[i][j] == 'g':
            gx, gy = j, i

que = deque()
que.append((sx, sy))
s[sy][sx] = 0
while que:
    x, y = que.popleft()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < w and 0 <= ny < h and s[ny][nx] == float("inf"):
            if c[ny][nx] == "#":
                s[ny][nx] = s[y][x] + 1
                que.append((nx, ny))
            else:
                s[ny][nx] = s[y][x]
                que.appendleft((nx, ny))

print("YES" if s[gy][gx] <= 2 else "NO")
