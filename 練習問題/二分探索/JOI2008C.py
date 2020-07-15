from bisect import bisect_right

n, m = map(int, input().split())
P = [0] + [int(input()) for _ in range(n)]
P.sort()

T = [P[i] + P[j] for i in range(n+1)
     for j in range(i, n+1) if P[i] + P[j] <= m]
T.sort()

ans = 0
for t in T:
    s = T[bisect_right(T, m-t) - 1]
    ans = max(ans, t+s)

print(ans)
