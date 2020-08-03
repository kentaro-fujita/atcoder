A, B, C, K = map(int, input().split())

ans = 0
ans += min(K, A) * 1
K -= A

ans += max(0, min(K, B)) * 0
K -= B

ans += max(0, min(K, C)) * -1
print(ans)
