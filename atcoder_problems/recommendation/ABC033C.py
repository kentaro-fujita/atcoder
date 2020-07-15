s = input()

ans = 0
for eq in s.split('+'):
    if '0' not in eq:
        ans += 1

print(ans)
