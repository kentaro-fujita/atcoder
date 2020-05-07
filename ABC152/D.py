N = int(input())

num =[[0] * 10 for _ in range(10)]

for n in range(1, N+1):
    s = str(n)
    a, b = map(int, [s[0], s[-1]])
    num[a][b] += 1

ans = 0
for a in range(1, 10):
    for b in range(1, 10):
        ans += num[a][b] * num[b][a]

print(ans)