N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9 + 7

cnt = 0
pair = 0
for i in range(N):
    for j in range(i+1, N):
        if A[i] > A[j]:
                cnt += 1

    for j in range(N):
        if A[j] > A[i]:
            pair += 1

v = (K * (K-1) // 2) % mod * pair % mod
print((cnt * K % mod + v) % mod)
