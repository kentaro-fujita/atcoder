n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]
a.reverse()

s = set()
for v in a:
    if v not in s:
        s.add(v)
        print(v)

for j in range(1, n+1):
    if j not in s:
        print(j)
