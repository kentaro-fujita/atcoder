s = list(input())
t = list(input())
n = len(s)
m = len(t)

ans = []
for i in range(n - m + 1):
    flag = True
    for j in range(m):
        if s[i+j] == t[j] or s[i+j] == '?':
            continue
        flag = False
    if flag:
        ans.append("".join(s[:i] + t + s[i+m:]).replace('?', 'a'))

if ans:
    print(min(ans))
else:
    print("UNRESTORABLE")
