N = int(input())
W = [int(input()) for _ in range(N)]

L = []
for w in W:
    flag = False
    for i, l in enumerate(L):
        if l[-1] >= w:
            flag = True
            L[i].append(w)
            break

    if not flag:
        L.append([w])

print(len(L))
