from collections import deque

def bfs():
    d = [[float("inf")] * m for i in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(n):
        for j in range(m):
            if maze[i][j] == "S":
                sx = i
                sy = j
            if maze[i][j] == "G":
                gx = i
                gy = j
    
    que = deque([])
    que.append((sx,sy))
    d[sx][sy] = 0

    while que:
        p = que.popleft()
        if p[0] == gx and p[1] == gy:
            break

        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != "#" and d[nx][ny] == float("inf"):
                que.append((nx,ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    return d[gx][gy]

n, m = map(int, input().split())
maze = [list(input()).split() for _ in range(n)]

print(bfs())