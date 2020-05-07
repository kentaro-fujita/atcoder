from bisect import bisect_left

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(N):
    a = L[i]
    for j in range(i+1, N):
        b = L[j]

        k = bisect_left(L, a+b)
        ans += max(k - (j+1), 0)

print(ans)
