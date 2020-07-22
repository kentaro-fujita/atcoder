from collections import deque

n, m = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    que = deque()
    d = [[float("inf")] * m for _ in range(n)]
    que.append([sx-1, sy-1])
    d[sy-1][sx-1] = 0

    while que:
        px, py = que.popleft()
        if px == gx-1 and py == gy-1:
            break
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] != '#' and d[ny][nx] == float("inf"):
                que.append((nx, ny))
                d[ny][nx] = d[py][px] + 1
    return d[gy-1][gx-1]


print(bfs())
