N = int(input())

Xr = []
Xb = []
for i in range(N):
    x, c = input().split()
    if c == 'R':
        Xr.append(int(x))
    if c == 'B':
        Xb.append(int(x))

Xr.sort()
for x in Xr:
    print(x)

Xb.sort()
for x in Xb:
    print(x)
