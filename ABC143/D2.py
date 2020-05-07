N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(N):
    k = i
    for j in range(i+1, N):
        while (k < N and L[k] < L[i]+L[j]):
            k += 1
        ans += k - (j+1)

print(ans)
