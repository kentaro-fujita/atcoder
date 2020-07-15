t = int(input())

ans = []
for _ in range(t):
    l, n = map(int, input().split())
    x = list(map(int, input().split()))

    res1 = 0
    res2 = 0
    for i in range(n):
        res1 = max(res1, min(x[i], l-x[i]))
        res2 = max(res2, max(x[i], l-x[i]))
    ans.append([res1, res2])

for a in ans:
    print(*a)
