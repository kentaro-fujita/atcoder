n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(n):
    if i == n-1 and i+1 == p[i]:
        ans += 1
    elif i+1 == p[i]:
        temp = p[i]
        p[i] = p[i+1]
        p[i+1] = temp
        ans += 1

print(ans)
