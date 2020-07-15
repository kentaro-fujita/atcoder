MAX = 10**6 + 1

sq = []
osq = []
i = 0
while (i+1) * (i+2) * (i+3) // 6 <= MAX:
    sq.append((i+1) * (i+2) * (i+3) // 6)
    if sq[i] % 2 == 0:
        osq.append(sq[i])
    i += 1

dp = [float("inf")] * MAX
dp[0] = 0
for i in range(MAX):
    for j in range(len(sq)):
        if i + sq[j] >= MAX:
            break
        dp[i+sq[j]] = min(dp[i+sq[j]], dp[i]+1)

odp = [float("inf")] * MAX
odp[0] = 0
for i in range(MAX):
    for j in range(len(osq)):
        if i + osq[j] >= MAX:
            break
        odp[i+osq[j]] = min(dp[i+osq[j], odp[i]+1])

while True:
    n = int(input())
    if n == 0:
        break

    print(f"{dp[n]} {odp[n]}")
