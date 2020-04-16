S = input()
n = len(S)

ans = 0
for i in range(1,n+1):
    for j in range(n-i+1):
        target = S[j:j+i]
        flag = True
        for t in target:
            if t not in ['A', 'C', 'G', 'T']:
                flag = False
                break
            
        if flag:
            ans = max(ans, len(target))

print(ans)
