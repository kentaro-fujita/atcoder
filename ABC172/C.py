from bisect import bisect_right

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
csa = [0] * (n+1)
for i in range(n):
    csa[i+1] += csa[i] + a[i]
csb = [0] * (m+1)
b = list(map(int, input().split()))
for i in range(m):
    csb[i+1] += csb[i] + b[i]

ans = 0
for i in range(n+1):
    t = k - csa[i]
    if t < 0:
        break
    j = bisect_right(csb, t)
    ans = max(ans, i + j - 1)

print(ans)
