from collections import deque

N, X, Y = map(int, input().split())

g = [[0] * 500 for _ in range(500)]
for i in range(N):
    x, y = map(int, input().split())
    g[y+250][x+250] = 1

d = [[-1] * 500 for _ in range(500)]
dxdy = [(1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (0, -1)]

que = deque([(0, 0)])
d[250][250] = 0
while que:
    x, y = que.popleft()
    if x == X and y == Y:
        break

    for dx, dy in dxdy:
        nx = x + dx
        ny = y + dy
        if -240 <= nx <= 240 and -240 <= ny <= 240 and d[ny+250][nx+250] == -1 and g[ny+250][nx+250] != 1:
            d[ny+250][nx+250] = d[y+250][x+250] + 1
            que.append((nx, ny))

print(d[Y+250][X+250])
