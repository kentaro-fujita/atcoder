n = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]

ans = 0
for i in range(6):
    ans += n // coins[i]
    n %= coins[i]

print(ans)
