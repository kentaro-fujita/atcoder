n = int(input())
a = list(map(int, input().split()))

m = 0
b = []
for i in range(n):
    if a[i] < 0:
        m += 1
        b.append(-a[i])
    else:
        b.append(a[i])

if m % 2 == 1:
    print(sum(b) - 2*min(b))
else:
    print(sum((b)))
