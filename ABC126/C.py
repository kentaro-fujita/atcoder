N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
    k = 0
    while i*2**k < K:
        k += 1
    ans += (1/N)*(1/2)**k

print(ans)