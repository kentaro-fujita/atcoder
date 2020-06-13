n = int(input())

f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = -float("inf")
for i in range(1, 2**10):
    isOpen = []
    for j in range(10):
        if i & (1<<j):
            isOpen.append(1)
        else:
            isOpen.append(0)
    res = 0
    for j in range(n):
        cnt = 0
        for k in range(10):
            if isOpen[k] and f[j][k]:
                cnt += 1
        res += p[j][cnt]
    ans = max(ans, res)

print(ans) 
