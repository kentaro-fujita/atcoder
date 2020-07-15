from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

unique = set()
for card in permutations(cards, k):
    unique.add(int("".join(card)))

print(len(unique))
