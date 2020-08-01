n = int(input())
s = [input() for _ in range(n)]

ans = []
a = 0
b = n - 1
while a <= b:
    left = False
    for i in range(b - a + 1):
        if s[a + i] < s[b - i]:
            left = True
            break
        elif s[a + i] > s[b - i]:
            left = False
            break
    if left:
        ans.append(s[a])
        a += 1
    else:
        ans.append(s[b])
        b -= 1
print("".join(ans))
