n = int(input())
a = list(map(int, input().split()))

r = 1
ans = 0
for l in range(n):
    while r < n and (r <= l or a[r-1] < a[r]):
        r += 1
    ans += r - l
    if l == r:
        r += 1

print(ans)
