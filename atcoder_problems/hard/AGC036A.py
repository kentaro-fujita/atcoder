import math

s = int(input())

x1 = math.ceil(math.sqrt(s))
y1 = 1
x2 = x1**2 - s
y2 = x1
x3 = 0
y3 = 0

print(x1, y1, x2, y2, x3, y3)
