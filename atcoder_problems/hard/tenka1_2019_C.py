n = int(input())
s = list(input())

cnt = [s.count('.'), s.count('#')]

cnt0 = 0
cnt1 = 0
ans = float("inf")
for i in range(n):
    if s[i] == '.':
        cnt0 += 1
    if s[i] == '#':
        cnt1 += 1
    ans = min(ans, cnt1 + cnt[0] - cnt0)

if ans > min(cnt):
    print(min(cnt))
else:
    print(ans)
