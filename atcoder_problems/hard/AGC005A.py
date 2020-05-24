x = input()
n = len(x)

ans = 0
cnt = 0
for i in range(n):
    if x[i] == 'S':
        cnt += 1
        ans += 1
    else:
        if cnt > 0:
            cnt -= 1
            ans -= 1
        else:
            ans += 1

print(ans)
