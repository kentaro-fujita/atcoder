# cppでの想定解だが，python3だとTLEになる

M, N = map(int, input().split())
K = int(input())
a = [list(input()) for _ in range(M)]

s = [[[0] * 3 for _ in range(N+1)] for _ in range(M+1)]
e = ['J', 'O', 'I']
for i in range(M):
    for j in range(N):
        for k in range(3):
            s[i+1][j+1][k] = s[i][j+1][k] +s[i+1][j][k] - s[i][j][k]

            if a[i][j] == e[k]:
                s[i+1][j+1][k] += 1

for i in range(K):
    a, b, c, d = map(int, input().split())

    ans = []
    for j in range(3):
        ans.append(s[c][d][j] - s[a-1][d][j] - s[c][b-1][j] + s[a-1][b-1][j])
    print(*ans)
