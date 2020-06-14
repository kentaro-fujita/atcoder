from collections import defaultdict

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

cnt = defaultdict(int)
for i in range(h):
    for j in range(w):
        cnt[a[i][j]] += 1

flag1 = w % 2
flag2 = h % 2
even = h * flag1 + w * flag2 - flag1 * flag2 * 2
odd = flag1 * flag2

ans = True
for k, v in cnt.items():
    even -= ((v % 4) // 2) * 2
    odd -= v % 2
    if even < 0 or odd < 0:
        ans = False
        break

print("Yes" if ans else "No")
