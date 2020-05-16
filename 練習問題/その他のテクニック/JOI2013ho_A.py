n = int(input())
s = list(map(int, input().split()))

cnt = 1
counts = []
for i in range(1, n):
    if s[i-1] != s[i]:
        cnt += 1
    else:
        counts.append(cnt)
        cnt = 1
counts.append(cnt)

ans = 0
m = len(counts)
if m < 3:
    print(sum(counts))
else:
    for i in range(m-2):
        ans = max(ans, counts[i]+counts[i+1]+counts[i+2])
    print(ans)
