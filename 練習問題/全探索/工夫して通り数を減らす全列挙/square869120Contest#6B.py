from statistics import median

N = int(input())
 
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

midA = int(median(A))
midB = int(median(B))

ans = 0
for i in range(N):
    ans += abs(A[i]-midA) + abs(B[i]-midB) + abs(B[i]-A[i])

print(ans)