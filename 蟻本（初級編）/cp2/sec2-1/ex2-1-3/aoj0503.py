from collections import deque

ans = []
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    state = 0
    for i in range(3):
        _, *cups = map(int, input().split())
        for cup in cups:
            state += i * 3**(cup-1)
    res = -1
    d = [-1] * 3**n
    que = deque([state])
    d[state] = 0
    while que:
        state = que.popleft()
        if state == 0 or state == 3**n - 1:
            res = d[state]
            break
        if d[state] > m:
            break

        state_copy = state
        tops = [-1] * 3
        for cup in range(n):
            tray = state_copy % 3
            state_copy //= 3
            tops[tray] = cup
        dt = [[1], [-1, 1], [-1]]
        for i, top in enumerate(tops):
            if top != -1:
                for di in dt[i]:
                    if top > tops[i + di]:
                        next_state = state + di * 3**top
                        if d[next_state] == -1:
                            d[next_state] = d[state] + 1
                            que.append(next_state)
    ans.append(res)

for a in ans:
    print(a)
