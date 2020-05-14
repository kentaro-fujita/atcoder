N = int(input())
A = list(map(int, input().split()))

s = [0] * (N+1)
for i in range(N):
    s[i+1] = s[i] + A[i]

for k in range(1, N+1):
    ans = 0
    for i in range(N-k+1):
        ans = max(ans, s[k+i] - s[i])
    print(ans)
