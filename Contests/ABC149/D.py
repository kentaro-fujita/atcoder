N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())
hands = {'r': 'p', 'p': 's', 's': 'r'}

ans = 0
h = []
for i in range(N):
    e = T[i]
    if i >= K and h[i-K] == hands[e]:
        h.append(None)
        continue

    if e == 'r':
        h.append('p')
        ans += P
    elif e == 'p':
        h.append('s')
        ans += S
    elif e == 's':
        h.append('r')
        ans += R

print(ans)
