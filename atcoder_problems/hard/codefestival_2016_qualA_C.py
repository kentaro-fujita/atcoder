s = list(input())
n = len(s)
k = int(input())

for i in range(n):
    x = ord(s[i]) - ord('a')
    if x == 0 or 26 - x > k: continue
    k -= 26 - x
    s[i] = 'a'

if k:
    s[-1] = chr((ord(s[-1]) - ord('a') + k) % 26 + ord('a'))

print(''.join(s))
