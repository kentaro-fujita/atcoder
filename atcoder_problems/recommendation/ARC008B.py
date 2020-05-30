import math
from collections import Counter

n, m = map(int, input().split())
name = input()
kit = input()

cnt_name = Counter(name)
cnt_kit = Counter(kit)

ans = 0
for k, v in cnt_name.items():
    if cnt_kit[k] == 0:
        print(-1)
        exit()
    else:
        ans = max(ans, math.ceil(v/cnt_kit[k]))

print(ans)
