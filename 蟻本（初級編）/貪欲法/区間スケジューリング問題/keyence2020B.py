n = int(input())
xl = [list(map(int, input().split())) for _ in range(n)]
le = [[p[0]-p[1], p[0]+p[1]] for p in xl]
le.sort(key=lambda x: x[1])

ans = 0
right = -(10 ** 9) - 1
for i in range(n):
    if right <= le[i][0]:
        ans += 1
        right = le[i][1]

print(ans)
