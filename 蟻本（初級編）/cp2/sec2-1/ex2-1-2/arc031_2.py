import copy

a = [list(input()) for _ in range(10)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    c[y][x] = 'x'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10 and c[ny][nx] == 'o':
            dfs(nx, ny)


for i in range(10):
    for j in range(10):
        if a[i][j] == 'x':
            c = copy.deepcopy(a)
            c[i][j] = 'o'
            s = [[0] * 10 for _ in range(10)]
            cnt = 0
            for y in range(10):
                for x in range(10):
                    if c[y][x] == 'o':
                        dfs(x, y)
                        cnt += 1
            if cnt == 1:
                print("YES")
                exit()

print("NO")
