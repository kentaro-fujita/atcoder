s = input()

ans = 0
for eq in s.split('+'):
    if not '0' in eq:
        ans += 1
    
print(ans)
