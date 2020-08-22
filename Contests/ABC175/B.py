n = int(input())
l = list(map(int, input().split()))

ans = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            if l[i] != l[j] and l[j] != l[k] and l[i] != l[k]:
                a, b, c = sorted([l[i], l[j], l[k]])
                if a + b > c:
                    ans.append([i, j, k])


print(len(set(frozenset(i) for i in ans)))
