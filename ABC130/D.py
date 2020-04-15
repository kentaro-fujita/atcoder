N, K = map(int, input().split())
a = list(map(int,input().split()))

res = 0

right = 0
sum_ = 0
for left in range(N):
    while right < N and sum_ < K:
        sum_ += a[right]
        right += 1
    if sum_ < K:
        break

    res += N - right + 1

    if right == left:
        right += 1
    else:
        sum_ -= a[left]

print(res)