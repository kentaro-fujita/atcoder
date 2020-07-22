from itertools import permutations

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]

ans = set()
for perm in permutations(cards, k):
    ans.add("".join(map(str, perm)))

print(len(ans))
