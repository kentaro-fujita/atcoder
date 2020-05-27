n, k = map(int, input().split())
d = list(map(int, input().split()))

a = []
for i in range(10):
    if i not in d:
        a.append(i)

check = set(a)
for i in range(10**5):
    if i >= n and set(map(int, list(str(i)))) <= set(a):
        print(i)
        exit()
