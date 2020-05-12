N = int(input())
P = list(map(int, input().split()))

ans = 0
min_ = P[0]
for i in range(N):
    if min_ >= P[i]:
        ans += 1
    min_ = min(min_, P[i])

print(ans)
