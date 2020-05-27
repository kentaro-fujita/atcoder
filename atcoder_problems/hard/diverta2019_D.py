n = int(input())

ans = 0
for k in range(1, int(n**(1/2))+1):
    m = (n - k) // k
    if m <= 0: continue
    if n // m == n % m:
        ans += m

print(ans)
