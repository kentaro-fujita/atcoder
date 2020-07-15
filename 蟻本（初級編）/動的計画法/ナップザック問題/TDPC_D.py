n, d = map(int, input().split())

count2 = 0
count3 = 0
count5 = 0
while d % 2 == 0:
    d //= 2
    count2 += 1
while d % 3 == 0:
    d //= 3
    count3 += 1
while d % 5 == 0:
    d //= 5
    count5 += 1

if d != 1:
    print(0)
    exit()

dp = [[[[0] * (count5 + 1) for _ in range(count3 + 1)]
       for _ in range(count2 + 1)] for _ in range(n+1)]
dp[0][0][0][0] = 1

d2 = [0, 1, 0, 2, 0, 1]
d3 = [0, 0, 1, 0, 0, 1]
d5 = [0, 0, 0, 0, 1, 0]

for i in range(n):
    for c2 in range(count2 + 1):
        for c3 in range(count3 + 1):
            for c5 in range(count5 + 1):
                for j in range(6):
                    nc2 = min(count2, c2 + d2[j])
                    nc3 = min(count3, c3 + d3[j])
                    nc5 = min(count5, c5 + d5[j])
                    dp[i + 1][nc2][nc3][nc5] += dp[i][c2][c3][c5] / 6

print(dp[n][count2][count3][count5])
