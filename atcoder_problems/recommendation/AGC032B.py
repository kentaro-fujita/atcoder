n = int(input())
d = n
ans = []
if n % 2 == 1: d -= 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if j <= i or j == d: continue
        ans.append([i, j])
    d -= 1

print(len(ans))
for f, s in ans:
    print(f, s)
