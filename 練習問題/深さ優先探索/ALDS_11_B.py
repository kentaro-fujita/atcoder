from collections import deque

n = int(input())

g = [deque([]) * n for _ in range(n)]

for i in range(n):
    u, k, *V = list(map(int, input().split()))
    V.sort()
    for v in V:
        g[u-1].append(v-1)
        # g[v-1].append(u-1)

time = 0
arrive_time = [-1] * n
finish_time = [-1] * n


def dfs(v):
    global time
    time += 1
    stack = [v]
    arrive_time[v] = time
    while stack:
        v = stack[-1]
        if g[v]:
            w = g[v].popleft()
            if arrive_time[w] < 0:
                time += 1
                arrive_time[w] = time
                stack.append(w)
        else:
            time += 1
            finish_time[v] = time
            stack.pop()

    return [arrive_time, finish_time]


for i in range(n):
    if arrive_time[i] < 0:
        ans = dfs(i)

for j in range(n):
    temp = [j+1, ans[0][j], ans[1][j]]
    print(*temp)
