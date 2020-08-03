n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = [0]
for i in range(n):
    top = a[i]
    if i == 0:
        ans.append(top)
    elif i != n - 1:
        ans += [top] * 2

print(sum(ans[:n]))
