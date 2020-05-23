n = int(input())
s = input()

left = 0
p = 0
for i in range(n):
    if s[i] == '(':
        p += 1
    else:
        if p == 0:
            left += 1
        else:
            p -= 1
right = p

res = ""
for i in range(left):
    res += '('
res += s
for i in range(right):
    res += ')'
print(res)
