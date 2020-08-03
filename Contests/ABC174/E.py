n, k = map(int, input().split())
a = list(map(int, input().split()))


def check(l):
    cnt = 0
    for L in a:
        cnt += L // mid
        if L % mid != 0:
            cnt += 1
        cnt -= 1

    return cnt <= k


lb, ub = 0, max(a)
while ub - lb > 1:
    mid = (ub + lb) // 2

    if check(mid):
        ub = mid
    else:
        lb = mid

print(ub)
