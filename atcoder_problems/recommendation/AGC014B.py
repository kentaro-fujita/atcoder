n, m = map(int, input().split())

c = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    c[a-1] += 1
    c[b-1] += 1

for i in range(n):
    if c[i] % 2 == 1:
        print("NO")
        exit()
print("YES")
