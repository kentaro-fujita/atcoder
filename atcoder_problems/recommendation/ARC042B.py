sx, sy = map(int, input().split())
n = int(input())

xy = [list(map(int, input().split())) for _ in range(n)]
xy.append(xy[0])

ans = float("inf")
for i in range(1, n+1):
    x1, y1 = xy[i-1]
    x2, y2 = xy[i]

    a = y2 - y1
    b = x1 - x2
    c = (x2 - x1) * y1 - (y2 - y1) * x1
    d = abs(a*sx + b*sy + c)/(a**2 + b**2)**0.5
    ans = min(ans, d)

print(ans)
