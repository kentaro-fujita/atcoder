s = input()

ans = 0
left = 0
right = len(s) - 1
while left < right:
    if s[left] == s[right]:
        left += 1
        right -= 1
    elif s[left] == 'x':
        left += 1
        ans += 1
    elif s[right] == 'x':
        right -= 1
        ans += 1
    else:
        ans = -1
        break

print(ans)
