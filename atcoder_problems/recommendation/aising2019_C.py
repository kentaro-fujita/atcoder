import sys
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

seen = [[0] * w for _ in range(h)]

dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

global ans
def dfs(x, y):
    seen[y][x] = 1
    a, b = 1, 0
    for dx, dy in dxdy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] and s[y][x] != s[ny][nx]:
            p = dfs(nx, ny)
            a += p[1]
            b += p[0]
    
    return (a, b)

ans = 0
for i in range(h):
    for j in range(w):
        if not seen[i][j]:
            p = dfs(j, i)
            ans += p[0] * p[1]
print(ans)
