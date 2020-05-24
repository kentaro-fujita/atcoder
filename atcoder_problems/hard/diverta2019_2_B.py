from itertools import combinations
from collections import defaultdict

n = int(input())

xy = [0] * n
for i in range(n):
    xy[i] = list(map(int, input().split()))

conter = defaultdict(int)
for com in combinations(range(n), 2):
    x1, y1 = xy[com[0]]
    x2, y2 = xy[com[1]]
    conter[(x2-x1, y2-y1)] += 1
    conter[(x1-x2, y1-y2)] += 1

ans = 0
for k, v in conter.items():
    ans = max(ans, v)

print(n - ans)
