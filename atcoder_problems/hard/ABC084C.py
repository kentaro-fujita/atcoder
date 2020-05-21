n = int(input())

c = [0] * (n-1)
s = [0] * (n-1)
f = [0] * (n-1)
for i in range(n-1):
    c[i], s[i], f[i] = list(map(int, input().split()))

for i in range(n):
    t = 0
    for j in range(i, n-1):
        if t < s[j]:
            t += (s[j] - t) + c[j]
        else:
            tmp = (t - s[j]) % f[j]
            if tmp == 0:
                t += c[j]
            else:
                t += (f[j] - tmp) + c[j]
    print(t)
