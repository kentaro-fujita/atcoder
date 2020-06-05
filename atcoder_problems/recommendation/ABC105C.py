n = int(input())

ans = []
while n:
    r = n % 2
    if r < 0:
        r += 2
    ans.append(str(r))
    n = (n-r) // -2
ans.reverse()

if len(ans) == 0:
    print(0)
else:
    print("".join(map(str, ans)))
