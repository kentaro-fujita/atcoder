from collections import Counter

N = int(input())
s = [''.join(sorted(input())) for _ in range(N)]

ans = 0
for i in Counter(s).values():
    ans += i * (i - 1) // 2

print(ans)
