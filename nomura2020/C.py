n = int(input())
a = list(map(int, input().split()))

m = [0] * (n+1)
mx = 1
for i in range(n+1):
    mx -= a[i]
    m[i] = mx

    if (mx <= 0 and i != n) or (mx < 0 and i == n):
        print(-1)
        exit()
    mx *= 2

a.reverse()
m.reverse()
m[0] = a[0]
for i in range(1, n+1):
    m[i] = min(m[i], m[i-1]) + a[i]

print(sum(m))
