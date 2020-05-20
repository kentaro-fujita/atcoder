n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 0
right = 0
sum_ = 0
for left in range(n):
    while right < n and sum_ < k:
        sum_ += a[right]
        right += 1
    if sum_ >= k:
        res += n - right + 1

    sum_ -= a[left]

print(res)
