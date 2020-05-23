n, k = map(int, input().split())

a = n // k
b = (n + (k//2)) // k
if k % 2 == 0:
    print(a**3 + b**3)
else:
    print(a**3)
