s = list(input())
n = len(s)

ans = []
for i in range(n):
    if s[i] == '0':
        ans.append('0')
    if s[i] == '1':
        ans.append('1')
    if s[i] == 'B':
        if ans:
            ans.pop()

print("".join(ans))
