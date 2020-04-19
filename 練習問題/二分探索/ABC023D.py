N = int(input())
H = [0] * N
S = [0] * N
 
for i in range(N):
    H[i], S[i] = map(int, input().split())
 
 
def ok(v):
    tmp = sorted([((v - H[i]) / S[i]) for i in range(N)])
 
    for i in range(N):
        if tmp[i] < i:
            return False
    return True
 
 
l = -1
r = 10 ** 15
while r - l > 1:
    mid = (r + l) // 2
    if ok(mid):
        r = mid
    else:
        l = mid
 
print(r)