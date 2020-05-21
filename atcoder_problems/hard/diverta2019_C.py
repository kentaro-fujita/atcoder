n = int(input())

ans = 0
cntA = 0
cntB = 0
cntBA = 0
for i in range(n):
    s = input()
    ans += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        cntBA += 1
    elif s[-1] == 'A':
        cntA += 1
    elif s[0] == 'B':
        cntB += 1
if cntBA == 0:
    ans += min(cntA, cntB)
elif cntA + cntB == 0:
    ans += cntBA - 1
else:
    ans += cntBA + min(cntA, cntB)

print(ans)
