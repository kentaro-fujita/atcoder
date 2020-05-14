N, M = map(int, input().split())
P = list(map(int, input().split()))

s = [0] * (N+2)
for i in range(M-1):
    d, t = P[i], P[i+1]
    s[min(d,t)] += 1
    s[max(d,t)] -= 1

for i in range(N):
    s[i+1] += s[i]

ans = 0
for i in range(1, N):
    A, B, C = map(int, input().split())
    if s[i] >= 1:
        if s[i] * A < s[i] * B + C:
            ans += s[i] * A
        else:
            ans += s[i] * B + C

print(ans)
