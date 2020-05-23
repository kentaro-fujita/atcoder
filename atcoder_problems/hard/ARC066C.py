from collections import defaultdict

mod = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

cnt = defaultdict(int)
for i in range(n):
    cnt[a[i]//2] += 1

ans = 1
for i, v in cnt.items():
    if v % 2 == 1 and i != 0:
        print(0)
        exit()
    else:
        ans *= v % mod

print(ans % mod)
