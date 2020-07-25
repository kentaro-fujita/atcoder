v = [1, 5, 10, 50, 100, 500]

c = map(int, input().split())
a = int(input())

ans = 0
for i in range(4, -1, -1):
    t = min(a // v[i], v[i])
    a -= t * v[i]
    ans += t
print(ans)
