n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7

neg = []
pos = []
for i in range(n):
    if a[i] < 0:
        neg.append(a[i])
    if a[i] > 0:
        pos.append(a[i])

neg.sort()
pos.sort(reverse=True)
nm = len(neg)
cp_neg = [1] * (nm + 1)
if neg:
    cp_neg[1] = neg[0]
    for i in range(1, nm):
        cp_neg[i+1] = neg[i-1] * neg[i]

pm = len(pos)
cp_pos = [1] * (pm + 1)
if pos:
    cp_pos[1] = pos[0]
    for i in range(1, pm):
        cp_pos[i+1] = pos[i-1] * pos[i]

print(cp_neg, cp_pos)
ans = 0
for i in range(k+1):
    if i <= nm and k - i <= pm:
        ans = max(ans, cp_neg[i] * cp_pos[k-i])

print(ans % mod)
