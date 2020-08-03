from fractions import gcd
n, m = map(int, input().split())
a = [int(i) for i in input().split()]
a = sorted(list(set(a)))

lc = a[0]
if n != 1:
    for num, i in enumerate(a[1:]):
        if lc == 0:
            break
        lc = lc * i // gcd(lc, i)
        if gcd(lc, i) == min(i, lc):
            for j in a[:num+1]:
                if (i/j) % 2 == 0:
                    lc = 0
                    break
if lc == 0:
    print(0)
else:
    print((m+lc//2)//lc)
