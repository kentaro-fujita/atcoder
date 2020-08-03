N = int(input())
S = [input() for _ in range(N)]

unique = set()

for s in S:
    unique.add(s)

print(len(unique))
