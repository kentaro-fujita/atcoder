A, B, X = map(int, input().split())

left = 0
right = 10**9 + 1
while right - left > 1:
    mid = (left + right) // 2
    f = A * mid + B * len(str(mid)) 
    if f > X:
        right = mid
    else:
        left = mid
    
print(left)
