n = int(input())
m = 10**6
mod = 10007

t = [0] * m
t[2] = 1
for i in range(3, m):
    t[i] = (t[i-1] + t[i-2] + t[i-3]) % mod

print(t[n-1] % mod)
