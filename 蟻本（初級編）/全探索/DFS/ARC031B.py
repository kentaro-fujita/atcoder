import copy

def dfs(x,y):
    field[x][y] = 'x'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < 10 and 0 <= ny and ny < 10 and field[nx][ny] == "o":
            dfs(nx,ny)

A = [list(input()) for _ in range(10)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(10):
    for j in range(10):
        if A[i][j] == "x":
            field = copy.deepcopy(A)
            field[i][j] = "o"
            count = 0
            for p in range(10):
                for q in range(10):
                    if field[p][q] == "o":
                        dfs(p,q)
                        count += 1

            if count == 1:
                print("YES")
                exit()

print("NO")