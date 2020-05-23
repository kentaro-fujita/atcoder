import math

n, h = map(int, input().split())

a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
m = max(a)
b.sort(reverse=True)

ans = 0
for i in range(n):
    if m <= b[i]:
        h -= b[i]
        ans += 1
        if h <= 0:
            print(ans)
            exit()

ans += math.ceil(h / m)
print(ans)
