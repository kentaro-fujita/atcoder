from collections import defaultdict

s = list(input())
n = len(s)

cnt = defaultdict(list)

for i in range(n):
    cnt[s[i]].append(i)
ans = float("inf")
for k, l in cnt.items():
    res = l[0]
    for i in range(1, len(l)):
        res = max(res, l[i] - l[i-1] - 1)
    res = max(res, n - l[-1] - 1)
    ans = min(ans, res)

print(ans)
