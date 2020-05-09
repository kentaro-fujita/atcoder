N, K = map(int, input().split())
S = list(input())

count = 0
for i in range(1, len(S)):
    if S[i-1] == S[i]:
        count += 1

print(min(count+2*K, len(S)-1))
