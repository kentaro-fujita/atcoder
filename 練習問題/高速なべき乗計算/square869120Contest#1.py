N , Q = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

mod = 10**9 + 7

path = [0]
dist = 0
for i in range(1, N):
    dist += pow(A[i-1], A[i], mod)
    path.append(dist)

ans = 0
start = 0
for c in C:
    ans += abs(path[start] - path[c-1])
    start = c - 1
ans += abs(path[start] - path[0])

print(ans % mod)
