import sys
sys.setrecursionlimit(1000000)

def dfs(x, y):
    d[y][x] = 1

    for i in range(8):
        nx = x + dx[i//3]
        ny = y + dy[i%3]
        
        if 0 <= nx < w and 0 <= ny < h and c[ny][nx] == 1 and d[ny][nx] == 0:
            dfs(nx, ny)

dx = [-1, 1, 0]
dy = [-1, 1, 0]

ans = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    c = [[] for _ in range(h)]
    for i in range(h):
        c[i] = list(map(int, input().split()))

    d = [[0] * w for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1 and d[i][j] == 0:
                dfs(j, i)
                count += 1
    
    print(count)