n, m = map(int, input().split())

s = []
for i in range(m):
    s.append(list(map(int, input().split()))[1:])
p = list(map(int, input().split()))

ans = 0
for i in range(1<<n):
    isOn = []
    for j in range(n):
        if i & (1<<j):
            isOn.append(j+1)

    flag = True
    for j in range(m):
        count = 0
        for v in s[j]:
            if v in isOn:
                count += 1
        if count % 2 != p[j]:
            flag = False
    if flag:
        ans += 1

print(ans)
