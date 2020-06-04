x, y, w = input().split()
x = int(x) - 1
y = int(y) - 1
c = [list(input()) for _ in range(9)]

d = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1), 'RU': (1, -1), 'RD': (1, 1), 'LU': (-1, -1), 'LD': (-1, 1)}
dx, dy = d[w]

count = 0
ans = []
while count < 4:
    ans.append(c[y][x])
    if x + dx < 0 or 9 <= x + dx: 
        dx *= -1
    if y + dy < 0 or 9 <= y + dy:
        dy *= -1
    x += dx
    y += dy
    count += 1

print(''.join(map(str, ans)))
