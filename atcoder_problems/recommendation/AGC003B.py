n = int(input())
a = [int(input()) for _ in range(n)]

ans = 0
i = 0
while i < n:
    res = 0
    for j in range(i, n):
        if a[j] == 0: break
        res += a[j]
    ans += res // 2
    i = j + 1

print(ans)
