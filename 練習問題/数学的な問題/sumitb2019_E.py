N = int(input())
A = list(map(int, input().split()))

mod = 10**9 + 7

ans = 1
counter = [0] * 10**5
for i, a in enumerate(A):
    if a == 0:
        ans *= (3 - counter[a]) % mod
        counter[a] += 1
    else:
        ans *= (counter[a-1] -counter[a]) % mod
        counter[a] += 1

print(ans % mod)
