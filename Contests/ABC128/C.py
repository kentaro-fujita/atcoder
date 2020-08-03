N, M = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))

ans = 0
for i in range(1 << N):
    flag = True
    for j in range(M):
        s = ks[j][1:]
        count = 0
        for v in s:
            if i & (1 << (v - 1)):
                count += 1
        if count % 2 != p[j]:
            flag = False

    if flag:
        ans += 1

print(ans)
