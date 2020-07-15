from itertools import combinations

nx = []
while True:
    n, x = map(int, input().split())

    if n == 0 and x == 0:
        break
    else:
        nx.append((n, x))

for n, x in nx:
    ans = 0
    for comb in combinations(range(1, n+1), 3):
        if sum(comb) == x:
            ans += 1

    print(ans)
