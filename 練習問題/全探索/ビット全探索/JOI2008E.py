r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]

ans = 0
for i in range(1<<r):
    b = []
    for j in range(r):
        if i & (1<<j):
            b.append([0 if a[j][k] == 1 else 1 for k in range(c)])
        else:
            b.append(a[j][:])

    sum_ = 0
    for k in range(c):
        s =  sum([b[j][k] for j in range(r)])
        sum_ += max(s, r-s)
    
    ans = max(ans, sum_)

print(ans)