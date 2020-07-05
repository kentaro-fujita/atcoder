n = int(input())

ans = []
for i in range(11):
    if 1000 * i - n >= 0:
        ans.append(1000*i - n)

print(min(ans))
