H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

Left = [[0] * W for _ in range(H)]
for y in range(H):
    count = 0
    for x in range(W):
        if S[y][x] == '#':
            count = 0
        else:
            count += 1
        Left[y][x] = count

Right = [[0] * W for _ in range(H)]
for y in range(H):
    count = 0
    for x in range(W - 1, -1, -1):
        if S[y][x] == '#':
            count = 0
        else:
            count += 1
        Right[y][x] = count

Up = [[0] * W for _ in range(H)]
for x in range(W):
    count = 0
    for y in range(H):
        if S[y][x] == '#':
            count = 0
        else:
            count += 1
        Up[y][x] = count

Down = [[0] * W for _ in range(H)]
for x in range(W):
    count = 0
    for y in range(H - 1, -1, -1):
        if S[y][x] == '#':
            count = 0
        else:
            count += 1
        Down[y][x] = count

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        else:
            res = Left[i][j] + Right[i][j] + Up[i][j] + Down[i][j] - 3
            ans = max(ans, res)

print(ans)
