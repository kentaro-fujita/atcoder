from collections import Counter

n = int(input())
v = list(map(int, input().split()))

if len(set(v)) == 1:
    print(n // 2)
else:
    a = []
    b = []
    for i in range(n):
        if i % 2 == 0:
            a.append(v[i])
        else:
            b.append(v[i])
    c_a = Counter(a).most_common()
    c_b = Counter(b).most_common()

    if c_a[0][0] != c_b[0][0]:
        ans = n - c_a[0][1] - c_b[0][1]
    else:
        ans = min(n - c_a[0][1] - c_b[1][1], n - c_a[1][1] - c_b[0][1])
    
    print(ans)
