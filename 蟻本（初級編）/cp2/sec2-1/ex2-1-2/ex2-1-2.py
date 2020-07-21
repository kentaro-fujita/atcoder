n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]


def dfs(x, y):
    field[x][y] = '.'

    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 'W':
                dfs(nx, ny)


res = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == 'W':
            dfs(i, j)
            res += 1
print(res)
