n, k, m, r = map(int, input().split())
s = [int(input()) for _ in range(n-1)]

s.sort(reverse=True)

if r * k <= sum(s[:k]):
    print(0)
else:
    ans = r * k - sum(s[:k-1])
    if 0 <= ans <= m:
        print(ans)
    elif m < ans:
        print(-1)
