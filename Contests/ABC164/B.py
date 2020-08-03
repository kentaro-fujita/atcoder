A, B, C, D = map(int, input().split())

i = 0
while True:
    if i % 2 == 0:
        C -= B
    else:
        A -= D

    if A <= 0:
        print("No")
        break
    if C <= 0:
        print("Yes")
        break
    i += 1
