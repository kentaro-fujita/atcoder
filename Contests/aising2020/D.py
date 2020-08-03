n = int(input())
x = list(input())

count = x.count('1')
one_count = count - 1
zero_count = count + 1

one_mod = 0
zero_mod = 0
for b in x:
    if one_count:
        one_mod = (one_mod * 2 + int(b)) % one_count
    zero_mod = (zero_mod * 2 + int(b)) % zero_count

f = [0] * 2000001
pop_count = [0] * 200001
for i in range(1, 200001):
    pop_count[i] = pop_count[i//2] + i % 2
    f[i] = f[i % pop_count[i]] + 1

for i in range(n):
    if x[i] == '1':
        if one_count:
            nxt = one_mod
            nxt -= pow(2, n-i-1, one_count)
            nxt %= one_count
            print(f[nxt] + 1)
        else:
            print(0)
    if x[i] == '0':
        nxt = zero_mod
        nxt += pow(2, n-i-1, zero_count)
        nxt %= zero_count
        print(f[nxt] + 1)
