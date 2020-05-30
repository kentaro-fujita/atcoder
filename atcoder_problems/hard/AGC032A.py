n = int(input())
b = list(map(int, input().split()))

a = []
for i in range(n):
    p = -1
    for j in range(len(b)-1, -1, -1):
        if b[j] == j + 1:
            p = j + 1
            break
    if p == -1:
        print(-1)
        exit()
    a.append(p)
    b.remove(p)

a.reverse()
print('\n'.join(map(str, a)))
