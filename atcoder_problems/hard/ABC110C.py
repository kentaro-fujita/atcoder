from collections import defaultdict

s = input()
t = input()
n = len(s)

ms = defaultdict(str)
mt = defaultdict(str)
for i in range(n):
    if ms[s[i]] == '':
        ms[s[i]] = t[i]
    if mt[t[i]] == '':
        mt[t[i]] = s[i]
    if ms[s[i]] != t[i] or mt[t[i]] != s[i]:
        print("No")
        exit()

print("Yes")
