import functools
import fractions

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = max(a)

gcd = functools.reduce(fractions.gcd, a)
if k <= m and k % gcd == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
