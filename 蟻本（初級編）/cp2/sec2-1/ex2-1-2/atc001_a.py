import sys
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
s = [[0] * w for _ in range(h)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    s[y][x] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h and c[ny][nx] != '#' and s[ny][nx] == 0:
            dfs(nx, ny)


ans = False
for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            ans = dfs(j, i)

for i in range(h):
    for j in range(w):
        if c[i][j] == 'g' and s[i][j]:
            print("Yes")
            exit()

print("No")
