import math

A, B, H, M = map(int, input().split())

h = H / 12 * 360 + M / 2
m = M / 60 * 360

d = min(360 - abs(h-m), abs(h-m))
C = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(d)))

print(C)
