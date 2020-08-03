from collections import defaultdict
from bisect import bisect_left

S = input()
T = input()

count = defaultdict(list)
for i, s in enumerate(S):
    count[s] += [i]

idx = 0
cnt = 0
for t in T:
    idxs = count[t]
    if not idxs:
        print(-1)
        exit()
    i = bisect_left(idxs, idx)
    if i < len(idxs):
        idx = idxs[i] + 1
    else:
        idx = idxs[0] + 1
        cnt += 1

ans = cnt * len(S) + idx
print(ans)
