n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ab = sorted(ab, key = lambda x : x[1])

ans = 0
end = 0
for i in range(m):
    if ab[i][0] >= end:
        end = ab[i][1]
        ans += 1

print(ans)