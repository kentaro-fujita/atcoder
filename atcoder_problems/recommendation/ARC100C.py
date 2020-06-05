n = int(input())
a = list(map(int, input().split()))

c = [0] * n
for i in range(n):
    c[i] = a[i] - (i+1)

c.sort()
b = c[n//2]
ans = 0
for j in range(n):
    ans += abs(c[j] - b)

print(ans)
