x, n = map(int, input().split())
p = list(map(int, input().split()))

ans = 0
m = float("inf")
for i in range(-200, 200):
    if i not in p:
        if abs(i-x) < m:
            ans = i
            m = abs(i-x)

print(ans)
