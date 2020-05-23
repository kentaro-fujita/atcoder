from collections import defaultdict

def prime_factorize(n):
    res = []
    for i in range(2, int(n**(1/2))+1):
        if n % i != 0: continue
        num = 0
        while n % i == 0:
            num += 1
            n /= i
        res.append((i, num))
    if n != 1:
        res.append((n, 1))
    
    return res

mod = 10**9 + 7
n = int(input())

cnt = defaultdict(int)
for i in range(1,n+1):
    res = prime_factorize(i)
    for j, v in res:
        cnt[j] += v

ans = 1
for i, v in cnt.items():
    ans *= (v+1)
print(ans % mod)
