n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = float("inf")
for i in range(n-k+1):
    res = x[i+k-1] - x[i] + min(abs(x[i+k-1]), abs(x[i]))
    ans = min(ans, res)

print(ans)
