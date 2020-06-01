from collections import Counter

n = int(input())

l = []
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
    l.append(a[i])
    l.append(b[i])

l.sort()
cnt = Counter(l)
if cnt[l[1]] != 2 or cnt[l[-2]] != 2:
    print(l[-1] - l[1])
else:
    print(l[-1] - l[0])
