from collections import Counter

n = int(input())
d = list(map(int, input().split()))
mod = 998244353

c = Counter(d)

if d[0] != 0 or c[0] != 1:
    print(0)
    exit()

ans = 1
for i in range(1, max(d)+1):
    if i not in c:
        print(0)
        exit()
    ans *= pow(c[i-1], c[i], mod)

print(ans % mod)
