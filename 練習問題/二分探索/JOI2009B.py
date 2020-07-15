d = int(input())
n = int(input())
m = int(input())

D = [0] + [int(input()) for _ in range(n-1)]
D.sort()

K = [int(input()) for _ in range(m)]

ans = 0
for k in K:
    left, right = 0, n
    while right - left > 1:
        mid = (left + right) // 2
        if D[mid] <= k:
            left = mid
        else:
            right = mid
    if left+1 == n:
        ans += min(k-D[left], d-k)
    else:
        ans += min(k-D[left], D[left+1]-k)

print(ans)
