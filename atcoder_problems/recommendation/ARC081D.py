n = int(input())
s1 = list(input())
s2 = list(input())

mod = 1000000007

pre = 0
ans = 3
i = 0
while i < n:
    if s1[i] == s2[i]:
        if pre == 1:
            ans = ans * 2 % mod
        pre = 1
        i += 1
    else:
        if pre == 2:
            ans = ans * 3 % mod
        else:
            ans = ans * 2 % mod
        pre = 2
        i += 2

print(ans)
