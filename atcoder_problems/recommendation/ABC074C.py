A, B, C, D, E, F = map(int, input().split())

ans = []
memo = []
for a in range(31):
    for b in range(31):
        for c in range(100):
            for d in range(100):
                w = 100 * A * a + 100 * B * b
                s = C * c + D * d
                if  w + s > F: continue
                if E * w / 100 >= s and w + s != 0:
                    ans.append(100 * s / (w + s))
                    memo.append([w + s, s])

print(*memo[ans.index(max(ans))])
