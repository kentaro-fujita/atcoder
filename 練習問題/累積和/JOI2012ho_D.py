n, m = map(int, input().split())

s = [[0] * (i + 1) for i in range(n)]
for _ in range(m):
    a, b, x = map(int, input().split())
    s[a-1][b-1] = max(s[a-1][b-1], x+1)

ans = 0
for i in range(n):
    for j in range(i + 1):
        if i != n-1:
            s[i + 1][j] = max(s[i + 1][j], s[i][j] - 1)
            s[i + 1][j + 1] = max(s[i + 1][j + 1], s[i][j] - 1)

        if s[i][j]:
            ans += 1

print(ans)
