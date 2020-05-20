H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

dp = [[float("inf")] * W for _ in range(H)]
if s[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0

dxdy = [(1, 0), (0, 1)]
for y in range(H):
    for x in range(W):
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if nx >= W or ny >= H: continue
            if s[ny][nx] == '#' and s[y][x] == '.':
                dp[ny][nx] = min(dp[ny][nx], dp[y][x] + 1)
            else:
                dp[ny][nx] = min(dp[ny][nx], dp[y][x])

print(dp[-1][-1])
