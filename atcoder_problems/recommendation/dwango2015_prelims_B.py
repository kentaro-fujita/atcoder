s = input()
n = len(s)

ans = 0
cnt = 0
i = 0
while i < n:
    if s[i:i+2] == '25':
        cnt += 1
        i += 2
    else:
        ans += cnt * (cnt + 1) // 2
        cnt = 0
        i += 1
ans += cnt * (cnt + 1) // 2
print(ans)
