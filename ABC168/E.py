from collections import Counter

n = int(input())
mod = 10**9 + 7

AB = [0] * n
for i in range(n):
    A, B = list(map(int, input().split()))
    AB[i] = A * B

cnt = Counter(AB)
print(cnt)
res = 0
for k, v in cnt.items():
    if k > 0 and -k in cnt.keys():
        res += v * cnt[-k]

print(pow(2, n, mod) - res*(n-1) - 1)
