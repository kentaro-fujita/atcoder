import sys
sys.setrecursionlimit(10**6)

m = int(input())
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(i, j, count):
    s[j][i] = 0
    count += 1
    ans = count
    for x, y in zip(dx, dy):
        if 0 <= i+x < m and 0 <= j+y < n:
            if s[j+y][i+x] == 1:
                ans = max(ans, dfs(i+x, j+y, count))
    s[j][i] = 1
    return ans

ans = 0
for j in range(n):
    for i in range(m):
        if s[j][i] == 1:
            ans = max(ans, dfs(i, j, 0))

print(ans)