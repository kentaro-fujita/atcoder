from collections import deque

H, W, N = map(int, input().split())
c = ["X" * (W+2)]
for i in range(H):
    s = input()
    s_idx = s.find("S")
    if s_idx != -1:
        sx, sy = i + 1, s_idx + 1
    c.append("X" + s + "X")
c.append("X" * (W+2))

seen = [[-1] * (W+2) for _ in range(H+2)]


def bfs(sx, sy, goal):
    queue = deque([(sx, sy)])
    seen[sx][sy] = 0

    while queue:
        x, y = queue.popleft()
        if c[x][y] == str(goal):
            return x, y, seen[x][y]

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if seen[nx][ny] == -1 and c[nx][ny] != "X":
                seen[nx][ny] = seen[x][y] + 1
                queue.append((nx, ny))


ans = 0
for i in range(1, N+1):
    sx, sy, time = bfs(sx, sy, i)
    seen = [[-1] * (W+2) for _ in range(H+2)]
    ans += time

print(ans)
