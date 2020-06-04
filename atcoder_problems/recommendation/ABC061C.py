n, k = map(int, input().split())

ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))

ab.sort(key=lambda x: x[0])

cnt = 0
for a, b in ab:
    if cnt <= k <= cnt+b:
        print(a)
        exit()
    cnt += b
