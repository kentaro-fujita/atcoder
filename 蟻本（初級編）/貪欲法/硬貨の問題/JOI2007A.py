a = 1000 - int(input())

v = [1, 5, 10, 50, 100, 500]

ans = 0
for i in range(1, 7):
    t = a // v[-i]
    a -= t * v[-i]
    ans += t

print(ans)