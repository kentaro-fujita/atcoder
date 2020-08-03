N = int(input())
A = [0] + list(map(int, input().split()))

for i in range(N, 0, -1):
    A[i] = sum(A[i::i]) % 2
print(sum(A))

ans = [i for i, v in enumerate(A) if v]
print(*ans)
