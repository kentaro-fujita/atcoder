n, k = map(int, input().split())

unique = set()
for i in range(k):
    d = int(input())
    A = list(map(int, input().split()))

    for a in A:
        unique.add(a)

print(n-len(unique))
