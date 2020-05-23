n = int(input())
a = list(map(int, input().split()))
a.sort()

cs_a = [0] * n
cs_a[0] = a[0]
for i in range(n-1):
    cs_a[i+1] = cs_a[i] + a[i+1]

ans = 0
for i in range(n-1):
    if a[i+1] <= cs_a[i] * 2:
        ans += 1
    else:
        ans = 0

print(ans+1)
