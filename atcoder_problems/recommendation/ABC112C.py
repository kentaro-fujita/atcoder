n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]

for x, y, h in xyh:
    if h!= 0:
        x0, y0, h0 = (x, y, h)
        break

for i in range(101):
    for j in range(101):
        res = 1
        for x, y, h in xyh:
            if h == max(h0+abs(x0-i)+abs(y0-j)-abs(x-i)-abs(y-j), 0):
                res *= 1
            else:
                res *= 0
        if res:
            print(i, j, h0 + abs(x0-i) + abs(y0-j))
            exit()