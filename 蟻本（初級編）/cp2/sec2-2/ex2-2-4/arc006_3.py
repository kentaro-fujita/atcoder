n = int(input())
w = [int(input()) for _ in range(n)]

ans = [[w[0]]]
for i in range(1, n):
    flag = False
    for j in range(len(ans)):
        if ans[j][-1] >= w[i]:
            ans[j].append(w[i])
            flag = True
            break
    if not flag:
        ans.append([w[i]])
print(len(ans))
