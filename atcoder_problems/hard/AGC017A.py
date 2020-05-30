import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

n, p = map(int, input().split())
a = list(map(int, input().split()))

even = []
odd = []
for i in range(n):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

m = len(even)
count1 = 0
for i in range(m+1):
    count1 += comb(m, i)

k = len(odd)
count2 = 0
if p == 0:
    for i in range(0, k+1, 2):
        count2 += comb(k, i)
else:
    for i in range(1, k+1, 2):
        count2 += comb(k, i)

print(count1*count2)
