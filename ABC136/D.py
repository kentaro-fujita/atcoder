S = input()
N = len(S)

ans = [1] * N
for i in range(N - 1):
    if S[i] == S[i + 1] == "R":
        ans[i + 2] += ans[i]
        ans[i] = 0

for i in range(N - 1, 1, -1):
    if S[i] == S[i - 1] == "L":
        ans[i - 2] += ans[i]
        ans[i] = 0

print(*ans)
