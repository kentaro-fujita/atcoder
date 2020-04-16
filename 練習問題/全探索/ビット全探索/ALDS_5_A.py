n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

for m in M:
    flag = False
    for i in range(1<<n):
        ans = 0
        for j in range(n):
            if i & (1<<j):
                ans += A[j]
        if ans == m:
            flag = True
    
    if flag:
        print("yes")
    else:
        print("no")