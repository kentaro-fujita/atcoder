H, W, K, V = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

s = [[0] * (W+1) for _ in range(H+1)]
for i in range(H):
    for j in range(W):
        s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + A[i][j]

ans = 0
for h in range(1, H+1):
    for w in range(1, W+1):
        for i in range(H-h+1):
            for j in range(W-w+1):
                area = s[i+h][j+w] - s[i+h][j] - s[i][j+w] + s[i][j]
                if area+h*w*K <= V:
                    ans = max(ans, h*w)

print(ans)
