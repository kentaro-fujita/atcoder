N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

s = [0] * (N+1)
p = 1
h = []
for i in range(K):
    h.append(p)
    s[p] = 1
    p = A[p]

    if s[p] != 0:
        break

if i == K-1:
    print(p)
    exit()
else:
    period = len(h) - h.index(p)
    rem = (K - h.index(p)) % period
    print(h[h.index(p):][rem])
