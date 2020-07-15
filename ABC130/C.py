W, H, x, y = map(int, input().split())

count = 0
if 2 * x == W and 2 * y == H:
    ans = W * H / 2
    count = 1
else:
    ans = W * H / 2

print(ans, count)
