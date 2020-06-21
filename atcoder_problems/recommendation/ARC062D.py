s = list(input())
n = len(s)

ans = 0
cnt_g = 0
cnt_p = 0
for i in range(n):
    if cnt_p + 1 <= cnt_g:
        cnt_p += 1
        if s[i] == 'g':
            ans += 1
    else:
        cnt_g += 1
        if s[i] == 'p':
            ans -= 1

print(ans)
