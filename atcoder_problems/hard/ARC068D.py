from collections import Counter

n = int(input())
a = list(map(int, input().split()))

a.sort()
cnt = Counter(a)
ans = 0
for k, v in cnt.items():
    if v > 1:
        ans += v - 1

print(len(cnt) - ans % 2)
