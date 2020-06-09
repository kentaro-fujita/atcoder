n = int(input())

ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append((a+b, a, b))

ab.sort(key= lambda x:x[0])

ans = 0
for i in range(n):
    v, a, b = ab.pop()
    if i % 2 == 0:
        ans += a
    else:
        ans -= b

print(ans)
