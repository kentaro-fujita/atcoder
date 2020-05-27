s = input()
n = len(s)
ans = 0
cntA = 0
for i in range(n-1):
    if s[i] == 'A':
        cntA += 1
    elif s[i: i+2] == 'BC':
        ans += cntA
    elif i > 0 and s[i-1: i+1] == 'BC':
        continue
    else:
        cntA = 0

print(ans)
