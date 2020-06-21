from collections import defaultdict

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    
    divisors.sort()
    return divisors

n = int(input())
a = list(map(int, input().split()))

div1 = set(make_divisors(a[0]))
div2 = set(make_divisors(a[1]))
common = div1 | div2

cnt = defaultdict(int)
for i in range(n):
    for j in common:
        if a[i] % j == 0:
            cnt[j] += 1

for k, v in sorted(cnt.items(), reverse=True):
    if v == n or v == n-1:
        print(k)
        exit()