import sys
sys.setrecursionlimit(10**6)

ans = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    c = [list(map(int, input().split())) for _ in range(h)]
    s = [[0] * w for _ in range(h)]

    def dfs(x, y):
        s[y][x] = 1

        for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < w and 0 <= ny < h and c[ny][nx] == 1 and s[ny][nx] == 0:
                    dfs(nx, ny)

    res = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1 and s[i][j] == 0:
                dfs(j, i)
                res += 1
    ans.append(res)

for a in ans:
    print(a)
