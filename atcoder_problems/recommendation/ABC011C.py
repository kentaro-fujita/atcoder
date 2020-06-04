n = int(input())

ng = []
for i in range(3):
    ng.append(int(input()))

if n in ng:
    print("NO")
    exit()

for i in range(100):
    for j in [3, 2, 1]:
        if n - j not in ng:
            n -= j
            break

if n <= 0:
    print("YES")
else:
    print("NO")
