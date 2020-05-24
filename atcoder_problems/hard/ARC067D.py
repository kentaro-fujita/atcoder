n, a, b = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    d = x[i+1] - x[i]
    if a * d < b:
        ans += a * d
    else:
        ans += b

print(ans)
