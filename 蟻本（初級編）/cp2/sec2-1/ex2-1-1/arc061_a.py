s = list(input())
n = len(s)

ans = 0
for i in range(1 << (n-1)):
    form = ""
    for j in range(n-1):
        form += s[j]
        if i & 1 << j:
            form += "+"
    form += s[-1]
    ans += eval(form)

print(ans)
