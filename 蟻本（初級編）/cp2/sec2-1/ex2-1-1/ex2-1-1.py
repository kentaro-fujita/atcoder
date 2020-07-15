n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(1 << n):
    res = 0
    for j in range(n):
        if i & 1 << j:
            res += a[j]
    if res == k:
        print("Yes")
        exit()

print("No")
