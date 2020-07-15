from itertools import product

n = int(input())

L = []
for i in range(3, 10):
    L += list(product("753", repeat=i))

ans = 0
for l in L:
    if len(set(l)) == 3 and int("".join(l)) <= n:
        ans += 1

print(ans)
