from collections import Counter

N = int(input())
S = input()

counter = Counter(S)
r_count = counter['R']
g_count = counter['G']
b_count = counter['B']

ans = r_count * g_count * b_count
for i in range(N):
    for j in range(N):
        k = 2 * j - i
        if k > N-1:
            break
        if i < j < k and S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
            ans -= 1

print(ans)