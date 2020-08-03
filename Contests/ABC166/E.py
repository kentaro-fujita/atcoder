from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

memo = defaultdict(int)
ans = 0
for i, a in enumerate(A, 1):
    ans += memo[i - a]
    memo[a + i] += 1

print(ans)
