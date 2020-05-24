n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum_a = sum(a)
sum_b = sum(b)
if sum_a <= sum_b:
    cnt = 0
    for i in range(n):
        if a[i] > b[i]:
            cnt += a[i] - b[i]
        elif a[i] < b[i]:
            cnt -= (b[i] - a[i]) // 2
    if cnt <= 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
