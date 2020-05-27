from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cs = [0] * (n+1)
for i in range(n):
    cs[i+1] = cs[i] + a[i]


ans = 0
cnt = Counter(cs)
for k, v in cnt.items():
    if v > 1:
        ans += v * (v-1) // 2

print(ans)
