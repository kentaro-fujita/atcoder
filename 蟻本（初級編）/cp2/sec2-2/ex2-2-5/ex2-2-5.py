n = int(input())
l = [int(input()) for _ in range(n)]

ans = 0
while n > 1:
    mii1, mii2 = 0, 1

    if l[mii1] > l[mii2]:
        mii1, mii2 = mii2, mii1

    for i in range(2, n):
        if l[i] < l[mii1]:
            mii2 = mii1
            mii1 = i
        elif l[i] < l[mii2]:
            mii2 = i

    t = l[mii1] + l[mii2]
    ans += t

    if mii1 == n-1:
        mii1, mii2 = mii2, mii1
    l[mii1] = t
    l[mii2] = l[n-1]
    n -= 1
print(ans)
