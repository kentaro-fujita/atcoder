A, B, N = map(int, input().split())

ans = 0
if B > N:
    x = N
else:
    x = B-1

print(int(A*x/B) - A*int(x/B))
