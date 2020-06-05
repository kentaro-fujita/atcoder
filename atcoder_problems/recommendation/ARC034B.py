n = int(input())

ans = []
for i in range(9*18+1):
    if i == eval("+".join(str(n-i))):
        ans.append(n-i)
ans.sort()

print(len(ans))
for a in ans:
    print(a)
