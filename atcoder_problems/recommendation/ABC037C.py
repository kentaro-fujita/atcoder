n, k = map(int, input().split())
a = list(map(int, input().split()))

cs = [0] * (n+1)
for i in range(n):
    cs[i+1] = cs[i] + a[i]

ans = 0
for i in range(n-k+1):
    ans += cs[i+k] - cs[i]

print(ans)
