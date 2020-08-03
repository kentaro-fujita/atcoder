n, m = map(int, input().split())
A = list(map(int, input().split()))

if n < sum(A):
    print(-1)
else:
    print(n-sum(A))
