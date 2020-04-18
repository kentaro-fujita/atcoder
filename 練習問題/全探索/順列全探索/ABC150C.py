from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

for i, order in enumerate(permutations(range(1,N+1))):
    if list(order) == P:
        a = i
    if list(order) == Q:
        b = i

print(abs(a-b))