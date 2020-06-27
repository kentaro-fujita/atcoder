from collections import Counter

n = int(input())
s = input()
cnt = Counter(s)

ans = cnt['R'] * cnt['G'] * cnt['B']
for i in range(n):
    for j in range(n):
        k = 2 * j - i
        if k > n-1:
            break
        if i < j < k and s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
            ans -= 1

print(ans)
