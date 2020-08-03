n = int(input())
a = list(map(int, input().split()))

res = a[0]
for i in range(1, n):
    res ^= a[i]

ans = []
for i in range(n):
    ans.append(res ^ a[i])

print(*ans)
