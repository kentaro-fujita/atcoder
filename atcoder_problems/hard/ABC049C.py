s = list(input())
n = len(s)
temp = ['maerd', 'remaerd', 'esare', 'resare']
s.reverse()

i = 0
while i < n:
    flag = False
    for t in temp:
        if s[i:i+len(t)] == list(t):
            i += len(t)
            flag = True
            break

    if not flag:
        print("NO")
        exit()

print("YES")
