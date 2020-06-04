n, m = map(int, input().split())

s = [0] * n
s[0] = 1
b = [1] * n
for i in range(m):
    x, y = map(int, input().split())

    if s[x-1]:
        s[y-1] = 1
    if b[x-1] == 1:
        s[x-1] = 0
    
    b[x-1] -= 1
    b[y-1] += 1

ans = 0
for i in range(n):
    if s[i] and b[i]:
        ans += 1

print(ans)
