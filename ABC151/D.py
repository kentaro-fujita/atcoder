from collections import deque

H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy):
    d = [[-1] * W for _ in range(H)]

    que = deque([])
    que.append((sx, sy))
    d[sy][sx] = 0

    res = 0
    while que:
        x, y = que.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < W and 0 <= ny < H and d[ny][nx] == -1 and c[ny][nx] == '.':
                que.append((nx, ny))
                tmp = d[y][x] + 1
                d[ny][nx] = tmp
                res = max(res, tmp)

    return res

ans = 0
for i in range(H):
    for j in range(W):
        if c[i][j] == '.':
            tmp = bfs(j, i)
            ans = max(ans, tmp)

print(ans)
