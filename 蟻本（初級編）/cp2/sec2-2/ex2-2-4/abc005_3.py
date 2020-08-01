t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_cnt = 0
b_cnt = 0
while a_cnt < n and b_cnt < m:
    if a[a_cnt] <= b[b_cnt] <= a[a_cnt] + t:
        a_cnt += 1
        b_cnt += 1
    else:
        a_cnt += 1

if b_cnt == m:
    print("yes")
else:
    print("no")
