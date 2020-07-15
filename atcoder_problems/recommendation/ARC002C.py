n = int(input())
cmd = input()

bs = ['X', 'Y', 'A', 'B']
scs = [x+y for x in bs for y in bs]

ans = float('inf')
for l in scs:
    for r in scs:
        score = 0
        idx = 0
        while idx < n:
            if idx == n-1:
                score += 1
                idx += 1
                continue
            s = cmd[idx] + cmd[idx+1]
            if s in (l, r):
                idx += 2
            else:
                idx += 1
            score += 1
        ans = min(ans, score)
print(ans)
