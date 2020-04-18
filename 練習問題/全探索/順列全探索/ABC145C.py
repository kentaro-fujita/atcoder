import math
from itertools import permutations

N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

d = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        dx = xy[i][0] - xy[j][0]
        dy = xy[i][1] - xy[j][1]
        d[i][j] = math.sqrt(dx**2 + dy**2)
        d[j][i] = math.sqrt(dx**2 + dy**2)

sum_ = 0
count = 0
for order in permutations(range(N)):
    for i in range(len(order)-1):
        sum_ += d[order[i]][order[i+1]]
    count += 1

print(sum_/count)