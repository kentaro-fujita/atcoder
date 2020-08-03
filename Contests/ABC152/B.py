a, b = input().split()

A = int(a * int(b))
B = int(b * int(a))

if A > B:
    print(A)
else:
    print(B)
