n = int(input())

s = 0
i = 0
while s < n:
    s += i
    i += 1

if i == 1:
    print(1)
else:
    ans = list(range(1,i))
    if s - n != 0: ans.remove(s-n)
    print('\n'.join(map(str,ans)))
