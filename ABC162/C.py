import math

K = int(input())

gcd = [[[0]* K for _ in range(K)] for _ in range(K)]

ans = 0
for a in range(K):
    for b in range(K):
        for c in range(K):
            if gcd[a][b][c] == 0:
                res = math.gcd(math.gcd(a+1,b+1),c+1)
                gcd[a][b][c] = res
                gcd[b][c][a] = res
                gcd[c][a][b] = res
                gcd[b][a][c] = res
                gcd[c][b][a] = res
                gcd[a][c][b] = res
                ans += res
            else:
                ans += gcd[a][b][c]

print(ans)