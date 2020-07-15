n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        xi, yi = xy[i]
        xj, yj = xy[j]
        ans = max(ans, ((xi-xj)**2 + (yi-yj)**2)**(1/2))

print(ans)
