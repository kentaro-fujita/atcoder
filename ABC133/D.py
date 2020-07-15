N = int(input())
A = list(map(int, input().split()))

X = [0] * N
X[0] = sum(A) - 2 * (sum([a for i, a in enumerate(A) if i % 2 == 1]))

ans = []
for i in range(N - 1):
    X[i + 1] = 2 * A[i] - X[i]

print(*X)
