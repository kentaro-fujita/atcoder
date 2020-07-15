from itertools import combinations

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for comb in combinations(range(M), 2):
    score = 0
    for i in range(N):
        score += max(A[i][comb[0]], A[i][comb[1]])

    ans = max(ans, score)

print(ans)
