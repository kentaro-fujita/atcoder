n = int(input())
c = list(input())

pos_r = []
pos_w = []
for i in range(n):
    if c[i] == 'R':
        pos_r.append(i)
    else:
        pos_w.append(i)
pos_r.reverse()

ans = 0
m = min(len(pos_r), len(pos_w))
for i in range(m):
    if pos_w[i] < pos_r[i]:
        ans += 1
print(ans)
