n = int(input())
a = list(map(int, input().split()))
a.sort()

m = a[-1]
res = m
temp = 0
for i in range(n):
    if res > abs(m - 2*a[i]):
        res = abs(m - 2*a[i])
        temp = a[i]

print(m, temp)
