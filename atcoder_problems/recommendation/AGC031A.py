from collections import Counter

n = int(input())
s = list(input())
mod = 10**9 + 7

cnt = Counter(s)

ans = 1
for k, v in cnt.items():
    ans *= (v + 1) % mod

print((ans - 1) % mod)
