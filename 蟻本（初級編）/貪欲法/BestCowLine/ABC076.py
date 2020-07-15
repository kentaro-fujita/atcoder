s = input()
t = input()

result = []
for i in range(len(s)-len(t)+1):
    temp = '?'*i + t + '?'*(len(s)-len(t)-i)

    ans = ''
    flag = True
    for j in range(len(s)):
        if s[j] == '?' or s[j] == temp[j]:
            ans += temp[j]
        elif s[j] != '?' and temp[j] == '?':
            ans += s[j]
        else:
            flag = False

    if flag:
        result.append(ans.replace('?', 'a'))

if result:
    result.sort()
    print(result[0])
else:
    print("UNRESTORABLE")
