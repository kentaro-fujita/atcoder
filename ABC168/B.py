K = int(input())
S = input()
N = len(S)

if N <= K:
    print(S)
else:
    print(S[:K] + '...')
