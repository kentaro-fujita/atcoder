mod = 10**5

n, m = map(int, input().split())
s = [int(input()) for _ in range(n-1)]

cs = [0] * n
for i in range(n-1):
    cs[i+1] = cs[i] + s[i]

ans = 0
now = 0
prev = 0
for i in range(m):
    now += int(input())
    ans += abs(cs[now] - cs[prev]) % mod
    prev = now

print(ans % mod)
