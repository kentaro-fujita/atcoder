n = int(input())
a = list(map(int, input().split()))
a.sort()
m = a[-1]

c = [0] * (m + 1)
for i in range(n):
    for j in range(a[i], m + 1, a[i]):
        c[j] += 1

ans = 0
for e in list(set(a)):
    if c[e] == 1:
        ans += 1

print(ans)
