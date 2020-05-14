n, m = map(int, input().split())

ans = float("inf")

x = [0] * (n+m)
y = [0] * (n+m)
r = [0] * (n+m)
for i in range(n):
    x[i], y[i], r[i] = map(int, input().split())
    ans = min(ans, r[i])

for i in range(m):
    x[n+i], y[n+i] = map(int, input().split())

for i in range(n, n+m):
    for j in range(n+i+1, n+m):
        d = (x[i]-x[j])**2 + (y[i]-y[j])**2
        ans = min(ans, d**(1/2)/2)

for i in range(n):
    for j in range(n, n+m):
        d = (x[i]-x[j])**2 + (y[i]-y[j])**2
        ans = min(ans, d**(1/2) - r[i])

print(ans)
