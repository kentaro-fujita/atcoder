n, k = map(int, input().split())
s = input()
s_sorted = sorted(s)

count = 0
for i in range(n):
    for c in s_sorted():
        tmp = 0
        if c != s[i]:
            tmp = 1
        else:
            tmp = 0
        
        t = s_sorted[:]
        t.remove(c)
        for j in range(i+1, n):
            if s[j] in t:
                t.remove(s[j])
            else:
                tmp += 1

            if count + tmp <= k:
                ans += c
                s_sorted.remove(c)
                if c != s[i]:
                    count += 1
                break

print(ans)