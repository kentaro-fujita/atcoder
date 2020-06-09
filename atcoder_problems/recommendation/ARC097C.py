s = list(input())
n = len(s)
k = int(input())

part = set()
for i in range(n):
    for j in range(k):
        part.add("".join(s[i:i+j+1]))

print(sorted(part)[k-1])
