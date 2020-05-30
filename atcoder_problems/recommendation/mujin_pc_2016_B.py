import math

l = list(map(int, input().split()))
l.sort()

r1 = sum(l)
s1 = math.pi * r1**2

if l[2] <= l[0] + l[1]:
    r2 = 0
else:
    r2 = l[2] - l[0] - l[1]
s2 = math.pi * r2**2

print(s1 - s2)
