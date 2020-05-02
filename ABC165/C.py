from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(Q)]

ans = 0
for comb in combinations_with_replacement(range(1,M+1), N):
    score = 0
    for a, b, c, d in abcd:
        if comb[b-1] - comb[a-1] == c:
            score += d
    ans = max(ans, score)

print(ans)