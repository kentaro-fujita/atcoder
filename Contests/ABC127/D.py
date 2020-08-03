N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(M)]
BC = sorted(BC, key=lambda x: x[1], reverse=True)

n = 0
for b, c in BC:
    n += b
    A += [c] * b

    if n >= N:
        break

A = sorted(A, reverse=True)
print(sum(A[:N]))
