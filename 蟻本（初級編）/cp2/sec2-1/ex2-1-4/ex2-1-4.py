import itertools

t = [i for i in range(4)]

print(list(itertools.permutations(t)))
print(list(itertools.permutations(t, 2)))
