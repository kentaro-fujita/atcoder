import sys
from collections import deque
sys.setrecursionlimit(10**7)

W, H = map(int, input().split())
c = [[0]*(W+2)]
for _ in range(H):
    c.append([0] + list(map(int, input().split())) + [0])
c.append([0] * (W+2))

s = [[-1] * (W+2) for _ in range(H+2)]

dxdyE = [(-1, -1), (0, -1), (-1, 0), (1, 0), (-1, 1), (0, 1)]
dxdyO = [(0, -1), (1, -1), (-1, 0), (1, 0), (0, 1), (1, 1)]

que = deque([(0, 0)])
s[0][0] = 0

ans = 0
while que:
    ix, iy = que.popleft()
    for dx, dy in (dxdyO if iy % 2 else dxdyE):
        nx = ix + dx
        ny = iy + dy

        if 0 <= nx < W+2 and 0 <= ny < H+2:
            if c[ny][nx] == 0 and s[ny][nx] == -1:
                s[ny][nx] = 1
                que.append((nx, ny))
            if c[ny][nx]:
                ans += 1
print(ans)
