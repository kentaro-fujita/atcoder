N = int(input())

A = [0] * N
xy = [[] for _ in range(N)]
for i in range(N):
    A[i] = int(input())
    xy[i] = [list(map(int, input().split())) for _ in range(A[i])]

ans = 0
for i in range(1 << N):
    honest = []
    unkind = []
    for j in range(N):
        if i & (1 << j):
            honest.append(j)
        else:
            unkind.append(j)

    flag = True
    for h in honest:
        for x, y in xy[h]:
            if y == 0 and (x-1) in unkind:
                continue
            if y == 1 and (x-1) in honest:
                continue

            flag = False

    if flag:
        ans = max(ans, len(honest))

print(ans)
